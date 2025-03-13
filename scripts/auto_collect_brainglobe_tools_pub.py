# This script fetches the citations of BrainGlobe's core publications using OpenAlex and
#  generates a Markdown file with the list of publications citing BrainGlobe's core publications. 
# The script is intended to be run periodically to keep the list of citations up-to-date. 
# The script outputs the generated Markdown file to the `docs/source/publications.md` file of the repository.
import pyalex
from datetime import datetime
from pathlib import Path

BRAINGLOBE_CORE_WORKS = [
    "https://openalex.org/W3138257762",
    "https://openalex.org/W3007765542",
    "https://openalex.org/W3165457844",
    "https://openalex.org/W3092644694",
    "https://openalex.org/W4206584351",
    "https://openalex.org/W3209832784",
    "https://openalex.org/W3165052512",
    "https://openalex.org/W3205056304"
    "https://openalex.org/W4408279592"
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
    """Process work while gracefully handling missing data"""
    entry = {
        "id": "", 
        "authors": "",
        "year": "",
        "title": "",
        "venue": "",
        "doi": "",
        "date": ""
    }
    
    if not work or not isinstance(work, dict):
        return entry

    try:
        # Capturing work ID 
        entry["id"] = work.get("id", "")

        # Handle truncated authorships
        if work.get("is_authors_truncated"):
            try:
                work = pyalex.Works()[work["id"]]
            except Exception:
                pass

        # Process authors
        authors = []
        for authorship in work.get("authorships", []):
            author = authorship.get("author", {})
            if author and isinstance(author, dict):
                authors.append(author.get("display_name", ""))
        
        if authors:
            author_str = ", ".join(authors[:3])
            if len(authors) > 3:
                author_str += " et al."
            entry["authors"] = author_str

        # Process title
        entry["title"] = work.get("title", "").strip()

        # Process venue
        source = work.get("primary_location", {}).get("source", {})
        entry["venue"] = source.get("display_name", "").split("(")[0].strip()

        # Process dates
        pub_date = work.get("publication_date", "")
        if pub_date:
            entry["date"] = pub_date
            try:
                entry["year"] = datetime.strptime(pub_date, "%Y-%m-%d").year
            except ValueError:
                pass

        # Process DOI
        entry["doi"] = work.get("doi", "")

    except Exception:
        pass

    return entry

def generate_markdown(works):
    """Generate clean Markdown output without error indications"""
    md = [
        "# BrainGlobe publications",

        "- **Eurasian blackcap (_Sylvia atricapilla_) atlas:**"
        "  > Sirmpilatze, N., Felder, A., Abdulazhanova, D., Schwigon, L., Haase, K., Musielak, I., Margrie, T. W., "
        "Mouritsen, H., Heyers, D., Tyson, A. L. , Weiler, S. (2025) "
        "\"Mapping the magnetoreceptive brain: A 3D digital atlas of the migratory bird Eurasian blackcap "
        "(Sylvia atricapilla) *bioRxiv* 2025.03.04.641293; "
        "doi: [doi.org/10.1101/2025.03.04.641293](https://doi.org/10.1101/2025.03.04.641293)"

        "- **Brainreg & brainglobe-segmentation (formerly brainreg-segment):**  ",
        "  > Tyson, A. L., Vélez-Fort, M., Rousseau, C. V., Cossell, L., Tsitoura, C., Lenzi, S. C., "
        "Obenhaus, H. A., Claudi, F., Branco, T., Margrie, T. W. (2022) "
        "\"Accurate determination of marker location within whole-brain microscopy images\" "
        "*Scientific Reports*, [doi.org/10.1038/s41598-021-04676-9](https://doi.org/10.1038/s41598-021-04676-9)\n",
        
        "- **3D cell detection:**  ",
        "  > Tyson, A. L., Rousseau, C. V., Niedworok, C. J., Keshavarzi, S., Tsitoura, C., Cossell, L., "
        "Strom, M., Margrie, T. W. (2021) "
        "\"A deep learning algorithm for 3D cell detection in whole mouse brain image datasets\" "
        "*PLOS Computational Biology* 17(5): e1009074. [doi.org/10.1371/journal.pcbi.1009074](https://doi.org/10.1371/journal.pcbi.1009074)\n",
        
        "- **Brainrender:**  ",
        "  > Claudi, F., Tyson, A. L., Petrucco, L., Margrie, T.W., Portugues, R., Branco, T. (2021) "
        "\"Visualizing anatomically registered data with Brainrender\" "
        "*eLife* 2021;10:e65751 [doi.org/10.7554/eLife.65751](https://doi.org/10.7554/eLife.65751)\n",
        
        "- **BrainGlobe Atlas API:**  ",
        "  > Claudi, F., Petrucco, L., Tyson, A. L., Branco, T., Margrie, T. W., Portugues, R. (2020) "
        "\"BrainGlobe Atlas API: a common interface for neuroanatomical atlases\" "
        "*Journal of Open Source Software* 5(54), 2668 [doi.org/10.21105/joss.02668](https://doi.org/10.21105/joss.02668)"
        "\n\n",
        "# Publications citing BrainGlobe",
        "**This list is automatically generated from [OpenAlex](https://openalex.org)**\n"
    ]

    # Sort works by date (newest first), with undated at end
    works.sort(key=lambda x: x["date"] if x["date"] else "0000-00-00", reverse=True)
    
    for work in works:
        entry = []
        # Add authors/year if available
        if work["authors"]:
            line = work["authors"]
            if work["year"]:
                line += f" ({work['year']})"
            entry.append(line)
        
        # Add title if available
        if work["title"]:
            entry.append(f"**{work['title']}**")
        
        # Add venue if available
        if work["venue"]:
            entry.append(f"*{work['venue']}*")
        
        # Add DOI link if available
        if work["doi"]:
            entry.append(f"[DOI](https://doi.org/{work['doi']})")
        
        if entry:
            md.append("  \n".join(entry))
    
    return "\n\n".join(md)

def main():
    print("Starting citation update...")
    
    # Create output directory structure using Path
    output_dir = Path("../docs") / "source"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Fetch and process citations
    works = fetch_citations()
    processed = [process_work(w) for w in works if w]
    
    # deduplication with core works exclusion
    seen = set()
    unique = []
    for w in processed:
        key = (w["title"].lower().strip(), w["year"])
        if (key not in seen 
            and w["title"]
            and w["id"] not in BRAINGLOBE_CORE_WORKS):  # Core works exclusion
            seen.add(key)
            unique.append(w)
    
    # citation counting
    complete_count = sum(1 for w in unique if w["doi"])
    total_publications = len(unique)
    
    # Generate and save output
    output_path = output_dir / "publications.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(generate_markdown(unique))
    
    # Status reporting
    print(f"Success! Updated {output_path} with {total_publications} publications:")
    print(f"- {complete_count} complete citations (with DOI)")
    print(f"- {total_publications - complete_count} incomplete citations (missing DOI)")
    print("Done!")

if __name__ == "__main__":
    main()
    