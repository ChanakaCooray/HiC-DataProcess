import os

import matplotlib.pyplot as plt
import networkx as nx
import powerlaw


# main func
def main(data):
    # chrm_list = list(range(1, 23))
    chrm_list = list(range(1, 23))
    chrm_list.append("X")

    for chr_n in chrm_list:
        chrm = "chr" + str(chr_n)

        rawdata_file = "RAWdata/" + data + "/50kb_resolution_intrachromosomal/" + chrm + "/MAPQGE30/" + chrm + "_50kb.RAWobserved"
        norm_file = "RAWdata/" + data + "/50kb_resolution_intrachromosomal/" + chrm + "/MAPQGE30/" + chrm + "_50kb.KRnorm"
        bin_size = 50000

        process_method0(rawdata_file, norm_file, bin_size, data, chrm)


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
                G.add_edge(index1, index2, weight=new_value)

    draw_powerlaw_graph(G, data, "powerlaw-normalized-" + chrm)


def process_method2(rawdata_file, norm_file, bin_size, data, chrm):
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

            G.add_edge(index1, index2, weight=value)

    draw_powerlaw_graph(G, data, "powerlaw-not-normalized-" + chrm)


def draw_powerlaw_graph(G, data, graph):
    degree_centrality = nx.degree_centrality(G)

    print(len(degree_centrality.values()))

    fit = powerlaw.Fit(list(degree_centrality.values()))

    # powerlaw.plot_pdf(list(degree_centrality.values()), linear_bins=True, color='r')
    fig2 = fit.plot_pdf(color='b', linewidth=2)
    fit.power_law.plot_pdf(color='b', linestyle='--', ax=fig2)
    fit.plot_ccdf(color='r', linewidth=2, ax=fig2)
    fit.power_law.plot_ccdf(color='r', linestyle='--', ax=fig2)

    # results.power_law.plot_pdf(color='b', linestyle='--')
    # results.plot_pdf(color='b')

    # print('alpha = ', results.power_law.alpha, '  sigma = ', results.power_law.sigma)

    plt.xlabel("alpha = {}, sigma = {}".format(fit.power_law.alpha, fit.power_law.sigma))

    # fig2 = fit.plot_pdf(color='b', linewidth=2)
    # fit.power_law.plot_pdf(color='b', linestyle='-', ax=fig2)

    # plt.show()

    plt.savefig(os.path.join("output/{}/powerlaw-distance-graphs".format(data), "{}.png".format(graph)))
    plt.clf()


if __name__ == '__main__':
    main("GM12878_primary")
