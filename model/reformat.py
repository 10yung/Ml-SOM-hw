import numpy as np

# concatenate nominal data title first N words
def title_concat(df, nChar):
    # process nominal data to Ove_TPC_TOS... format
    label_abbr = np.empty([1, len(df.index)], dtype=str)
    label_abbr[:] = ''

    for column in df:
        fist_two_char = np.array(df[column].astype(str).str[:nChar])
        string = '_'
        fist_two_char = [ string + x for x in fist_two_char]

        label_abbr = np.core.defchararray.add(label_abbr, fist_two_char)

    return label_abbr
