from imgproc_utils import *
from trace_utils import *
import csv
from skimage.feature import canny
import scipy.stats as stats
from distinctipy import distinctipy
from matplotlib.colors import to_hex, to_rgb 
plt.rcParams['svg.fonttype'] = 'none'

def show_all_traces(all_traces, genotypes=None, genes=None, color_dict=None):
    if genotypes is None:
        genotypes = list(all_traces.keys())
    
    if genes is None:
        genes = []
        for genotype in genotypes:
            genes += list(all_traces[genotype].keys())
        genes = list(set(genes))

    if color_dict is None:
        color_dict = get_color_dict(genotypes)
    
    fig, axs = plt.subplots(len(genes), 1, figsize=(10, 10*len(genes)))
    for ax, gene in zip(axs, genes):
        for genotype in genotypes:
            if gene not in all_traces[genotype].keys():
                continue
            traces = all_traces[genotype][gene]
            mean_traces = np.nanmean(traces, 1)
            n = mean_traces.shape[0]
            mean = np.nanmean(mean_traces, 0)
            error = np.nanstd(mean_traces, 0) / mean_traces.shape[0]
            ax.fill_between(np.arange(mean.shape[0]), mean-error, mean+error, alpha=0.5, linewidth=0, color=color_dict[genotype])
            ax.plot(mean, label=f'{genotype} (n = {n})', color=color_dict[genotype])
            ax.set_title(f'{gene} Mean Traces (w/ Std)')
            ax.legend()
    
    return fig

def get_color_dict(genotypes):
    color_dict = {}
    genotypes = genotypes.copy()
    if 'wt' in genotypes:
        color_dict['wt'] = '#000000'
        genotypes.remove('wt')

    if 'pho' in genotypes:
        color_dict['pho'] = '#B90E0A'
        genotypes.remove('pho')

    
    exclude = list(to_rgb(color) for color in color_dict.values())
    exclude.append(to_rgb('#ffffff'))

    colors = distinctipy.get_colors(len(genotypes), 
                                    exclude, 
                                    colorblind_type="Deuteranomaly")
    for color, genotype in zip(colors, genotypes):
        color_dict[genotype] = to_hex(color)
    
    return color_dict