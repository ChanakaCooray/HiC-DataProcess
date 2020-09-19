def main():
    a = ['hESC_r1', 'hESC_r2', 'IMR90_r1', 'IMR90_r2']

    for k in ('Original', 'Merged'):
        for i in range(0, 3):
            for j in range(i + 1, 4):
                out = open("R-hicrep-" + a[i] + "-" + a[j] + "-" + k + ".pbs", "w")

                out.write("#!/bin/bash\n" +
                          "#PBS -q default\n" +
                          "#PBS -N J_R" + a[i] + a[j] + "\n" +
                          "#PBS -l select=1:mem=8gb:ncpus=1\n" +
                          "#PBS -l walltime=08:00:00\n" +
                          "#PBS -W group_list=x-ccast-prj-luliu\n" +
                          "cd $PBS_O_WORKDIR\n" +
                          "module load R\n" +
                          "Rscript hicrep-process.R ../" + k + "/" + a[i] + "/" + " ../" + k + "/" + a[j] + "/" + " " + a[i] + " " + a[j] + "\n" +
                          "exit 0\n")
                out.close()


if __name__ == '__main__':
    main()
