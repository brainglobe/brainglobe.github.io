import pyalex
import os
from datetime import datetime

BRAINGLOBE_CORE_WORKS = [
    "https://openalex.org/W3138257762",
    "https://openalex.org/W3007765542",
    "https://openalex.org/W3165457844",
    "https://openalex.org/W3092644694",
    "https://openalex.org/W4206584351"
    "https://openalex.org/W3209832784"
    "https://openalex.org/W3165052512"
    "https://openalex.org/W3205056304"
]

pyalex.config.email = "hello@brainglobe.info"

def fetch_citations():
    """Fetch works citing BrainGlobe's core publications with pagination"""
    citing_works = []
    try:
        query = pyalex.Works().filter(cites="|".join(BRAINGLOBE_CORE_WORKS))
        for page in query.paginate(per_page=200, n_max=5):
            citing_works.extend([w for w in page if w and isinstance(w, dict)])
            print(f"Fetched {len(page)} citations...")
    except Exception as e:
        print(f"API Error: {str(e)}")
    return citing_works

def process_work(work):
    """Process work with comprehensive error tracking"""
    entry = {
        "authors": "Authors not available",
        "year": "",
        "title": "Untitled Work",
        "venue": "Unknown Source",
        "doi": "",
        "date": "",
        "errors": [],
        "status": "invalid"
    }
    
    if not work or not isinstance(work, dict):
        entry["errors"].append("Invalid work format")
        return entry

    try:
        # Handle truncated authorships
        if work.get("is_authors_truncated"):
            try:
                work = pyalex.Works()[work["id"]]
            except Exception as e:
                entry["errors"].append(f"Author fetch error: {str(e)}")

        # Process authors
        try:
            authors = []
            for authorship in work.get("authorships", []):
                author = authorship.get("author", {})
                if author and isinstance(author, dict):
                    authors.append(author.get("display_name", "Unknown Author"))
            
            if authors:
                author_str = ", ".join(authors[:3])
                if len(authors) > 3:
                    author_str += " et al."
                entry["authors"] = author_str
            else:
                entry["errors"].append("Missing authors")
        except Exception as e:
            entry["errors"].append(f"Author processing error: {str(e)}")

        # Process title
        try:
            entry["title"] = work.get("title", "Untitled Work").strip()
            if not entry["title"]:
                entry["errors"].append("Missing title")
        except Exception as e:
            entry["errors"].append(f"Title error: {str(e)}")

        # Process venue
        try:
            source = work.get("primary_location", {}).get("source", {})
            venue = source.get("display_name", "Preprint").split("(")[0].strip()
            entry["venue"] = venue
        except Exception as e:
            entry["errors"].append(f"Venue error: {str(e)}")

        # Process dates
        try:
            pub_date = work.get("publication_date", "")
            if pub_date:
                entry["date"] = pub_date
                entry["year"] = datetime.strptime(pub_date, "%Y-%m-%d").year
            else:
                entry["errors"].append("Missing publication date")
        except Exception as e:
            entry["errors"].append(f"Date error: {str(e)}")

        # Process DOI
        try:
            entry["doi"] = work.get("doi", "")
        except Exception as e:
            entry["errors"].append(f"DOI error: {str(e)}")

        # Validate entry
        if not entry["errors"]:
            entry["status"] = "valid"

    except Exception as e:
        entry["errors"].append(f"General processing error: {str(e)}")

    return entry

def generate_markdown(works):
    """Generate Markdown output with separate sections"""
    md = [
        "# Publications citing BrainGlobe",
        "**This list is automatically generated from OpenAlex**\n",
        "## Complete Publications\n"
    ]
    
    # Split works into complete and incomplete
    complete = [w for w in works if w["status"] == "valid"]
    incomplete = [w for w in works if w["status"] != "valid"]
    
    # Sort complete works by date (newest first)
    complete.sort(key=lambda x: x["date"], reverse=True)
    
    # Sort incomplete works by title
    incomplete.sort(key=lambda x: x["title"].lower())
    
    # Add complete works
    for work in complete:
        md.append(format_entry(work))
    
    # Add incomplete section if needed
    if incomplete:
        md.extend([
            "\n## Publications with Incomplete Metadata",
            "*The following entries may be missing some citation details:*\n"
        ])
        for work in incomplete:
            entry = format_entry(work)
            if work["errors"]:
                entry += f"\n*Missing data: {', '.join(work['errors'])}*"
            md.append(entry)
    
    return "\n\n".join(md)

def format_entry(work):
    """Format individual work entry"""
    entry = f"{work['authors']}"
    if work["year"]:
        entry += f" ({work['year']})"
    entry += f". **{work['title']}**  \n"
    entry += f"*{work['venue']}*  \n"
    if work["doi"]:
        entry += f"[DOI](https://doi.org/{work['doi']})  \n"
    return entry

def main():
    print("Starting citation update...")
    
    # Create output directory structure
    output_dir = os.path.join("../docs", "source")
    os.makedirs(output_dir, exist_ok=True)
    
    # Fetch and process citations
    works = fetch_citations()
    processed = [process_work(w) for w in works if w]
    
    # Deduplicate based on title/year
    seen = set()
    unique = []
    for w in processed:
        key = (w["title"].lower().strip(), w["year"])
        if key not in seen:
            seen.add(key)
            unique.append(w)
    
    # Generate and save output
    output_path = os.path.join(output_dir, "pub_citations.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(generate_markdown(unique))
    
    # Print summary
    complete_count = len([w for w in unique if w["status"] == "valid"])
    incomplete_count = len(unique) - complete_count
    print(f"Success! Updated {output_path} with:")
    print(f"- {complete_count} complete citations")
    print(f"- {incomplete_count} incomplete citations")

if __name__ == "__main__":
    main()
    