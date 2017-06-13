import numpy as np


def som_neuron_locations(m, n):
    for i in range(m):
        for j in range(n):
            yield np.array([i, j])

def clustered_location_input_index(m, n, som_result_map, input_data):
    filter_map_value = np.array(list(som_neuron_locations(m, n)))

    filter_map = []

    som_clusting_result_location_list = []
    for i in range(0, m * n * 2, 2):
        filter_map_tmp = np.stack([np.squeeze(filter_map_value.reshape((1, -1))) for i in range(len(input_data))])[
                             :, [i, i + 1]]
        # print(filter_map_tmp)
        myarray_tmp = np.array(np.squeeze(np.array(np.where(np.all(som_result_map == filter_map_tmp, axis=1)))))
        som_clusting_result_location_list.append(myarray_tmp.tolist())

    return som_clusting_result_location_list


