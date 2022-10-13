from imgproc_utils import *
from trace_utils import *
import csv
from skimage.feature import canny
import scipy.stats as stats
from distinctipy import distinctipy
from matplotlib import rcParams
from matplotlib.colors import to_hex, to_rgb 
import seaborn as sns

rcParams['svg.fonttype'] = 'none'
rcParams['font.family'] = ['Avenir']
rcParams['font.size'] = 16

def show_all_traces(all_traces, genotypes=None, genes=None, color_dict=None, individuals=False, zeroed=False, xlim=[5,95], normalize=False, ylim=None):
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

    if not isinstance(axs, np.ndarray): axs = [axs]
    for ax, gene in zip(axs, genes):
        for genotype in genotypes:
            if gene not in all_traces[genotype].keys():
                continue
            traces = all_traces[genotype][gene]
            mean_traces = np.nanmean(traces, 1)
            if zeroed:
                mean_traces -= np.nanmean(mean_traces[:, xlim[0]:xlim[1]], 0).min()
                #mean_traces -= np.nanmean(mean_traces, 0).min()
            if normalize:
                #mean_traces /= np.nanmean(mean_traces[:, xlim[0]:xlim[1]], 0).max()
                mean_traces /= np.nanmean(mean_traces, 0).max()
            n = mean_traces.shape[0]
            mean = np.nanmean(mean_traces, 0)

            if individuals:
                for trace in mean_traces:
                    ax.plot(trace, alpha=0.5, linewidth=0.5, color=color_dict[genotype])    
                ax.set_title(f'{gene} Individual Traces with Mean')
            else:
                error = np.nanstd(mean_traces, 0) / np.sqrt(mean_traces.shape[0])
                ax.fill_between(np.arange(mean.shape[0]), mean-error, mean+error, alpha=0.5, linewidth=0, color=color_dict[genotype])
                ax.set_title(f'{gene}')
            
            ax.plot(mean, label=f'{genotype} (n = {n})', color=color_dict[genotype])
        ax.legend(frameon=False)
        ax.set_xlim(xlim)
        ax.set_xlabel('Percent Embryo Length (%)')
        ax.set_ylabel('Intensity (a.u.)')
        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')
        if zeroed:
            ax.set_ylim(ymin=0)
        if ylim is not None:
            ax.set_ylim(ylim)
    
    return fig

def show_genotype_traces(all_traces, genotype='wt', genes=None, individuals=False, zeroed=False, xlim=[10,90], normalize=False):
    if genes is None:
        genes = list(all_traces[genotype].keys())
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    colors = plt.rcParams["axes.prop_cycle"].by_key()['color']
    for i, gene in enumerate(genes):
        if gene not in all_traces[genotype].keys():
            continue
        traces = all_traces[genotype][gene]
        mean_traces = np.nanmean(traces, 1)
        if zeroed:
            mean_traces -= np.nanmean(mean_traces[:, xlim[0]:xlim[1]], 0).min()
            #mean_traces -= np.nanmean(mean_traces, 0).min()
        if normalize:
            mean_traces /= np.nanmean(mean_traces[:, xlim[0]:xlim[1]], 0).max()
            #mean_traces /= np.nanmean(mean_traces, 0).max()
        n = mean_traces.shape[0]
        mean = np.nanmean(mean_traces, 0)
        if individuals:
            for trace in mean_traces:
                ax.plot(trace, alpha=0.5, linewidth=1, color=colors[i])
            ax.set_title(f'{gene} Individual Traces with Mean')
        else:
            error = np.nanstd(mean_traces, 0) / np.sqrt(mean_traces.shape[0])
            ax.fill_between(np.arange(mean.shape[0]), mean-error, mean+error, alpha=0.5, linewidth=0, color=colors[i])
            ax.set_title(f'{gene}')
        ax.plot(mean, label=f'{gene} (n = {n})', color=colors[i])
        ax.set_xlim(xlim)
        if zeroed:
            ax.set_ylim(ymin=0)
        ax.legend(frameon=False)
        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')
    return fig

def get_color_dict(genotypes):
    color_dict = {}
    genotypes = genotypes.copy()
    if 'wt' in genotypes:
        color_dict['wt'] = '#000000'
        genotypes.remove('wt')

    if 'pho' in genotypes:
        color_dict['pho'] = '#349B87'
        genotypes.remove('pho')

    if 'esc' in genotypes:
        color_dict['esc'] = '#882255'
        genotypes.remove('esc')
    
    # exclude = list(to_rgb(color) for color in color_dict.values())
    # exclude.append(to_rgb('#ffffff'))

    # # colors = distinctipy.get_colors(len(genotypes), 
    #                                 exclude, 
    #                                 colorblind_type="Deuteranomaly")
    # colors = sns.color_palette("rocket")

    # for colors, genotype in zip(colors, genotypes):
    #     color_dict[genotype] = to_hex(colors)
    return color_dict