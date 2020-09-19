def main():
    output_dir = ""
    n = 16

    for i in range(1, n + 1):
        out_file = output_dir + "/python-process-ambiguous-" + str(i) + ".pbs"
        out = open(out_file, "w")

        out.write(
            '#!/bin/bash\n#PBS -q default\n#PBS -N J_IMR-' + str(i) +
            '\n##serial jobs: only 1 processor core is requested\n#PBS -l select=1:mem=8gb:ncpus=1\n' +
            '#PBS -l walltime=24:00:00\n' +
            '##replace "x-ccast-prj" below with "x-ccast-prj-[your sponsor\'s project group]"\n' +
            '#PBS -W group_list=x-ccast-prj-luliu\n' +
            'cd $PBS_O_WORKDIR\n' +
            'python process-ambiguous.py --input IMR90_r1_1_m20-part-' + str(i) +
            ' --output output/IMR90_r1_1_m20-part-' + str(i) + '-output\nexit 0')

        out.close()


if __name__ == '__main__':
    main()
