import matplotlib
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def extract_country(recipe_tag):
    indicators = ['austrilian', 'chinese', 'korean', 'american',
                  'japanese', 'thai', 'italian', 'french', 'danish',
                  'swiss', 'swedish', 'german', 'namibian', 'argentine', 'nigerian', 'norwagian',
                  'new-zealand', 'lebanese', 'mexican', 'irish', 'canadian', 'hawaiian',
                  'indonesian', 'polish', 'caribbean', 'russian', 'iraqi', 'saudi-arabian', 'pakistani', 'scottish',
                  'south-african', 'cuban', 'columbian', 'finnish', 'iranian-persian', 'dutch', 'turkish',
                  'portuguese', 'hungarian', 'georgian', 'brazilian', 'nigerian', 'egyptian', 'chilean',
                  'vietnamese', 'palestinian', 'austrian', 'caribbean', 'greek', 'micro-melanesia', 'polynesian',
                  'spanish', 'malaysian', 'namibian', 'angolan', 'belgian', 'cambodian', 'british-columbian',
                  'californian', 'cantonese', 'central-american', 'chinese-new-year', 'costa-rican', 'czech',
                  'ethiopian', 'filipino', 'honduran', 'hunan', 'icelandic', 'irish-st-patricks-day', 'laotian',
                  'libyan', 'mongolian', 'moroccan', 'native-american',
                  'north-american', 'northeastern-united-states', 'oaxacan', 'ontario', 'quebec', 'puerto-rican',
                  'somalian',
                  'southern-united-states', 'sudanese', 'szechuan', 'welsh', 'venezuelan', 'indian', 'australian']

    dic = {'mexican': 'Mexico',
           'american': 'United States of America',
           'canadian': 'Canada',
           'hawaiian': 'Hawaii',
           'german': 'Germany',
           'italian': 'Italy',
           'polish': 'Poland',
           'danish': 'Denmark',
           'swiss': 'Switzerland',
           'swedish': 'Sweden',
           'caribbean': 'Caribbean',
           'greek': 'Greece',
           'russian': 'Russia',
           'micro-melanesia': 'Melanesia',
           'spanish': 'Spain',
           'irish': 'Ireland',
           'scottish': 'UK',
           'south-african': 'South Africa',
           'new-zealand': 'New Zealand',
           'finnish': 'Finland',
           'dutch': 'Netherlands',
           'portuguese': 'Portugal',
           'hungarian': 'Hungary',
           'brazilian': 'Brazil',
           'nigerian': 'Niger',
           'egyptian': 'Egypt',
           'argentine': 'Argentina',
           'chilean': 'Chile',
           'chinese': 'China',
           'saudi-arabian': 'Saudi Arabia',
           'turkish': 'Turkey',
           'japanese': 'Japan',
           'austrian': 'Austria',
           'palestinian': 'Palestine',
           'lebanese': 'Lebanon',
           'thai': 'Thailand',
           'indonesian': 'Indonesia',
           'italian': 'Italy',
           'pakistani': 'Pakistan',
           'cuban': 'Cuba',
           'malaysian': 'Malaysia',
           'vietnamese': 'Vietnam',
           'palestinian': 'Palestine',
           'namibian': 'Namibia',
           'iranian-persian': 'Iran',
           'polynesian': 'Polynesia',
           'iraqi': 'Iraq',
           'georgian': 'Georgia',
           'korean': 'South Korea',
           'french': 'France',
           'english': 'England',
           'austrilian': 'Austrilia',
           'norwagian': 'Norway',
           'angolan': 'Angola',
           'belgian': 'Belgium',
           'cambodian': 'Cambodia',
           'british-columbian': 'Canada',
           'californian': 'United States of America',
           'cantonese': 'China',
           'central-american': 'United States of America',
           'chinese-new-year': 'China',
           'costa-rican': 'Costa Rica',
           'czech': 'Czechia',
           'ethiopian': 'Ethiopia',
           'filipino': 'Philippines',
           'honduran': 'Honduras',
           'hunan': 'China',
           'icelandic': 'Iceland',
           'irish-st-patricks-day': 'Ireland',
           'laotian': 'Laos',
           'libyan': 'Libya',
           'mongolian': 'Mongolia',
           'moroccan': 'Morocco',
           'native-american': 'United States of America',
           'north-american': 'United States of America',
           'northeastern-united-states': 'United States of America',
           'oaxacan': "Mexico",
           'ontario': 'Canada',
           'quebec': 'Canada',
           'puerto-rican': 'Caribbean',
           'somalian': 'Somalia',
           'southern-united-states': 'United States of America',
           'sudanese': 'Sudan',
           'szechuan': 'China',
           'welsh': 'United Kingdom',
           'venezuelan': 'Venezuela',
           'indian': 'India',
           'australian': 'Australia'}

    dic_cc = {'Mexico': 'North America',
              'America': 'North America',
              'Canada': 'North America',
              'Hawaii': 'North America',
              'Germany': 'Europe',
              'Italy': 'Europe',
              'Poland': 'Europe',
              'Denmark': 'Europe',
              'Switzerland': 'Europe',
              'Sweden': 'Europe',
              'Caribbean': 'North America',
              'Greece': 'Europe',
              'Russia': 'Europe',
              'Melanesia': 'Oceania',
              'Spain': 'Europe',
              'Ireland': 'Europe',
              'United Kingdom': 'Europe',
              'South Africa': 'Africa',
              'New Zealand': 'Oceania',
              'Finland': 'Europe',
              'Netherlands': 'Europe',
              'Portugal': 'Europe',
              'Hungary': 'Europe',
              'Brazil': 'South America',
              'Niger': 'Africa',
              'Egypt': 'Africa',
              'Argentina': 'South America',
              'Chile': 'South America',
              'China': 'Asia',
              'Saudi Arabia': 'Asia',
              'Turkey': 'Asia',
              'Japan': 'Asia',
              'Austria': 'Europe',
              'Palestine': 'Asia',
              'Lebanon': 'Asia',
              'Thailand': 'Asia',
              'Indonesia': 'Asia',
              'Pakistan': 'Asia',
              'Cuba': 'South America',
              'Malaysia': 'Asia',
              'Vietnam': 'Asia',
              'Namibia': 'Africa',
              'Iran': 'Asia',
              'Polynesia': 'Oceania',
              'Iraq': 'Asia',
              'Georgia': 'Europe',
              'Korea': 'Asia',
              'France': 'Europe',
              'England': 'Europe',
              'Austrilia': 'Oceania',
              'Norway': 'Europe',
              'Angola': 'Africa',
              'Belgium': 'Europe',
              'Cambodia': 'Asia',
              'Costa Rica': 'North America',
              'Czechia': 'Europe',
              'Ethiopia': 'Africa',
              'Philippines': 'Asia',
              'Honduras': 'North America',
              'Iceland': 'Europe',
              'Laos': 'Asia',
              'Libya': 'Africa',
              'Mongolia': 'Asia',
              'Morocco': 'Africa',
              'Somalia': 'Africa',
              'Venezuela': 'South America',
              'Sudan': 'Africa',
              'India': 'Asia',
              'Australia': 'Oceania'
              }
    recipe_country = recipe_tag[recipe_tag['tags'].isin(indicators)]
    recipe_country.insert(2, "country", recipe_country['tags'].map(dic), True)
    recipe_country.drop(columns='tags', inplace=True)
    recipe_country.reset_index(drop=True, inplace=True)
    recipe_country.drop_duplicates(inplace=True)
    recipe_country.insert(3, "continent", recipe_country['country'].map(dic_cc), True)
    return recipe_country


def plt_wordcloud(data_list):
    word = ''
    for val in data_list:
        # typecaste each val to string
        val = str(val)
        word += val + ' '
    stopwords = set(STOPWORDS)

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          collocations=False,
                          min_font_size=10).generate(word)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()


# the following two functions are from the internet to help plot the heatmaps
# https://matplotlib.org/3.1.1/gallery/images_contours_and_fields/image_annotated_heatmap.html
# Use case:
# corres = data_feature_droped[athletic_skills].corr()
# fig, ax = plt.subplots(figsize=(10,10))
# fig.suptitle('Pearson correlation between different properties')
# im, cbar = heatmap(corres.values, corres.columns, corres.index, ax=ax,
#                    cmap="coolwarm", cbarlabel="pearson correlation")
# texts = annotate_heatmap(im, valfmt="{x:.3f}", threshold=0.7)
# fig.tight_layout()
# plt.show()


def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (N, M).
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw, fraction=0.046, pad=0.04)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[1] + 1) - .5, minor=True)
    ax.set_yticks(np.arange(data.shape[0] + 1) - .5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=["black", "white"],
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A list or array of two color specifications.  The first is used for
        values below a threshold, the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max()) / 2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts
