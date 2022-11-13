#!/usr/bin/env python

def fig_params():
    import matplotlib as mpl 
    import matplotlib.pyplot as plt
    linewidth_default = 2.0 
    fig_text_default = 13. 
    fig_title_default = fig_text_default*1.5
    plt.rc('title',)
    plt.rc('lines', linewidth=linewidth_default)
    plt.rc('text', usetex=False)
    plt.rc('font', size=fig_text_default, weight='normal',family='sans-serif')
    plt.rc('axes',titlesize=fig_title_default,titleweight='bold')
    plt.rcParams['figure.titlesize']=fig_title_default
    plt.rcParams["figure.titleweight"]='bold'
    mpl.rcParams['figure.dpi'] = 100 
    plt.rc('axes', labelsize=10)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=10)    # fontsize of the tick labels
