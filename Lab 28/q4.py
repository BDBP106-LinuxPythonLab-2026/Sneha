# 4) Creating and working with a GenBank file

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO

# Given plasmid sequence
plasmid_seq = Seq(
    "GGATCCTTATGGCTAGCAAAGGAGAAGAACTTTTCACTTAAGAATTCCC"
)

# 1. Create SeqRecord
record = SeqRecord(
    plasmid_seq,
    id="PLAB001",
    name="PLAB001",
    description="Cloning construct"
)

# Set molecule type
record.annotations["molecule_type"] = "DNA"


# Add three features

# BamHI site: positions 0-6
bamhi = SeqFeature(
    FeatureLocation(0, 6),
    type="misc_feature",
    qualifiers={"note": ["BamHI site"]}
)

# CDS: positions 8-41
cds = SeqFeature(
    FeatureLocation(8, 41),
    type="CDS",
    qualifiers={
        "gene": ["labA"],
        "translation": ["MASKGEELFT"]
    }
)

# EcoRI site: positions 41-47
ecori = SeqFeature(
    FeatureLocation(41, 47),
    type="misc_feature",
    qualifiers={"note": ["EcoRI site"]}
)

# Add features to record
record.features = [bamhi, cds, ecori]


# 2. Write GenBank file
SeqIO.write(record, "lab construct.gb", "genbank")

print("GenBank file created successfully!")


# 3. Read GenBank file
new_record = SeqIO.read("lab construct.gb", "genbank")

print("\nFeatures in GenBank file:")
print("Type\t\tStart\tEnd\tGene/Note")

for feature in new_record.features:

    # Convert Python coordinates to 1-based coordinates
    start = int(feature.location.start) + 1
    end = int(feature.location.end)

    # Get gene or note qualifier
    description = (
        feature.qualifiers.get("gene",
        feature.qualifiers.get("note", ["-"]))[0]
    )

    print(f"{feature.type}\t{start}\t{end}\t{description}")


# 4. Extract and translate CDS

cds_feature = [
    feature for feature in new_record.features
    if feature.type == "CDS"
][0]

cds_seq = cds_feature.extract(new_record.seq)

translated_protein = cds_seq.translate(to_stop=True)

stored_translation = cds_feature.qualifiers["translation"][0]

print("\nCDS sequence:", cds_seq)
print("Translated protein:", translated_protein)
print("Stored translation:", stored_translation)

# Check whether translations match
if str(translated_protein) == stored_translation:
    print("Translation matches!")
else:
    print("Translation does not match!")