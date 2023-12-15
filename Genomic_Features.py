import csv
import gzip
infile = "tuberculosis.gff"  #replace with desired gff file to look at genomic features

with gzip.open(infile,"rt") as fh:
    i=0
    features = {}
    gene_features = []
    csvin = csv.reader(fh,delimiter="\t")
    for line in csvin:
        if len(line) < 9:
            continue
#        if i > 500:
#            break
        start = int(line[3])
        end   = int(line[4])        
#        print(end - start)
        feature_length = end - start
        if line[2] == "gene":
            gene_features.append(feature_length)
        if line[2] not in features:
            features[line[2]] = []
        features[line[2]].append(feature_length)
#        print(line)
        i += 1
    #print(features)
    for ftype in features:
        count = len(features[ftype])
        avglen = sum(features[ftype]) / count
        print(f'There are {count} {ftype} with an avg length of {avglen}')        
    print(f'There are {len(gene_features)} genes with an avg length of {sum(gene_features) / len(gene_features)}')
