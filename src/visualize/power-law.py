import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import collections
import os

# main func
def main(data):
    chrm_list = list(range(1, 23))
    # chrm_list = list(range(1, 2))
    chrm_list.append("X")

    for chr_n in chrm_list:
        chrm = "chr" + str(chr_n)

        rawdata_file = "RAWdata/" + data + "/50kb_resolution_intrachromosomal/" + chrm + "/MAPQGE30/" + chrm + "_50kb.RAWobserved"
        norm_file = "RAWdata/" + data + "/50kb_resolution_intrachromosomal/" + chrm + "/MAPQGE30/" + chrm + "_50kb.KRnorm"
        bin_size = 50000

        process_method2(rawdata_file, norm_file, bin_size, data, chrm)


def process_method0(rawdata_file, norm_file, bin_size, data, chrm):
    i = 1
    norm_map = {}
    with open(norm_file) as f:
        for line in f:
            norm_map[i] = line.rstrip('\n')
            i += 1

    print(i)

    G = nx.Graph(name="Network")

    count = 0
    with open(rawdata_file) as f:
        for line in f:
            splitLine = line.split()

            bin1 = int(splitLine[0])
            bin2 = int(splitLine[1])
            value = float(splitLine[2])

            index1 = int((bin1 / bin_size) + 1)
            index2 = int((bin2 / bin_size) + 1)

            new_value = "NaN"
            if norm_map[index1] != "NaN" and norm_map[index2] != "NaN":
                new_value = value / (float(norm_map[index1]) * float(norm_map[index1]))

            if new_value != "NaN":
                count += 1
                G.add_edge(index1, index2, weight=new_value)

    print(count)

    draw_powerlaw_graph(G, data, "powerlaw-normalized-" + chrm)

def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b

def process_method2(rawdata_file, norm_file, bin_size, data, chrm):

    # G = nx.Graph(name="Network")
    network = {}
    count = 0
    with open(rawdata_file) as f:
        for line in f:
            splitLine = line.split()

            bin1 = int(splitLine[0])
            bin2 = int(splitLine[1])
            value = float(splitLine[2])

            if not isint(splitLine[2]):
                print("Error")

            index1 = int((bin1 / bin_size) + 1)
            index2 = int((bin2 / bin_size) + 1)

            # if index1==index2:
            #     continue

            count +=1

            if index1 not in network:
                network[index1] = int(value)
            else:
                network[index1] += int(value)

            if index2 not in network:
                network[index2] = int(value)
            else:
                network[index2] += int(value)

            # G.add_edge(index1, index2, weight=value)

    print(count)

    draw_powerlaw_graph(network, data, "degree-" + chrm)


def draw_powerlaw_graph(network, data, graph):
    # degree_centrality = nx.degree_centrality(G)

    # print(degree_centrality)

    # degree_sequence = [G.degree(n) for n in G.nodes()]
    # print(len(degrees))
    # print(sum(degrees))
    # print(np.mean(degrees))
    # plt.hist(degrees, bins=int(len(degrees)/100))

    # degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    # print "Degree sequence", degree_sequence
    # degree_centrality = sorted(degree_centrality, reverse=True)
    # degreeCount = collections.Counter(degree_centrality)

    # degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence

    # print(len(degree_sequence))
    # print(sum(degree_sequence))

    degreeCount = collections.Counter(network.values())
    deg, cnt = zip(*degreeCount.items())
    # deg, cnt = zip(*network.items())
    plt.scatter(deg,cnt, s=2)

    # plt.show()

    # degree_centrality = nx.degree_centrality(G)
    #
    # print(len(degree_centrality.values()))

    # fit = powerlaw.Fit(list(degree_centrality.values()))

    # powerlaw.plot_pdf(list(degree_centrality.values()), linear_bins=True, color='r')
    # fig2 = fit.plot_pdf(color='b', linewidth=2)
    # fit.power_law.plot_pdf(color='b', linestyle='--', ax=fig2)
    # fit.plot_ccdf(color='r', linewidth=2, ax=fig2)
    # fit.power_law.plot_ccdf(color='r', linestyle='--', ax=fig2)

    # results.power_law.plot_pdf(color='b', linestyle='--')
    # results.plot_pdf(color='b')

    # print('alpha = ', results.power_law.alpha, '  sigma = ', results.power_law.sigma)

    plt.xlabel("Degree")
    plt.ylabel("Frequency")

    # fig2 = fit.plot_pdf(color='b', linewidth=2)
    # fit.power_law.plot_pdf(color='b', linestyle='-', ax=fig2)

    # plt.show()

    plt.savefig(os.path.join("output/{}/powerlaw-distance-graphs/degree-histogram/with-diagonal".format(data), "{}.png".format(graph)))
    plt.clf()


if __name__ == '__main__':
    main("GM12878_primary")
