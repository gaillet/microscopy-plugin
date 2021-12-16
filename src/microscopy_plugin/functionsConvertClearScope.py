import numpy as np

def convert_coord_cs_to_xy(coordCS, dim_tile_horz, dim_tile_vert):
    coord_x = np.ceil(coordCS /dim_tile_horz)
    coord_y = np.absolute(np.mod(coordCS - dim_tile_horz - 1, 2 * dim_tile_horz) - dim_tile_horz + 0.5) + 0.5
    return coord_x, coord_y

def convert_coord_xy_to_cs(coord_x, coord_y, dim_tile_horz, dim_tile_vert):
    # test coord x and y are same size ?
    p_min_one = np.power(-1, coord_y)
    coord_cs =  dim_tile_horz * (coord_y + (p_min_one - 1)/2) - coord_x * p_min_one + (p_min_one + 1)/2
    return coord_cs

def getClearScopeRange2(dim_tile_horz, dim_tile_vert, range_x, range_y):

    # check that the dims of range_x and range_y are dims [2,1]
    size_vect = dim_tile_horz*dim_tile_vert
    coord_x = np.zeros(size_vect)
    coord_x = coord_x.astype(int)

    coord_y = np.zeros(size_vect)
    coord_y = coord_y.astype(int)

  # Modify function to use the two above functions: convert range to 2 single dime vectors that contains all the
  # x and y pairs: example: x E [1,3] y E [1,2] => x = [1 2 3 1 2 3] and y = [1 1 1 2 2 2]
    count = 1
    is_rising = 1
    for ind1 in range(size_vect):
      coord_y[ind1] = np.floor(ind1/dim_tile_horz) + 1

      coord_x[ind1] = count

      count = count + is_rising

      if count > dim_tile_horz or count < 1:
        is_rising = is_rising*(-1)
        count = count + is_rising
        coord_x[ind1] = count

    #array_clear_scope = np.empty(shape=(dimTiling[0],dimTiling[1]))
    #array_clear_scope.fill(0)

    mask_x = np.zeros(size_vect)
    mask_x = mask_x.astype(int)
    temp1 = np.where(coord_x < range_x[0], mask_x, mask_x + 1)
    temp2 = np.where(coord_x > range_x[1], mask_x, mask_x + 1)
    mask_x = temp1*temp2

    mask_y = np.zeros(size_vect)
    mask_y = mask_y.astype(int)
    temp1 = np.where(coord_y < range_y[0], mask_y, mask_y + 1)
    temp2 = np.where(coord_y > range_y[1], mask_y, mask_y + 1)
    mask_y = temp1*temp2

    mask_final = mask_x*mask_y
    indRange = mask_final*np.arange(1,size_vect+1)
    indRange = np.unique(indRange)

    return indRange[1:]

def getClearScopeRange(dim_tile_horz, dim_tile_vert, range_x, range_y):

    count = 0

    size_loop_x = range_x[1] - range_x[0] + 1
    size_loop_y = range_y[1] - range_y[0] + 1

    coord_x = np.zeros(size_loop_x * size_loop_y)
    coord_y = np.zeros(size_loop_x * size_loop_y)

    for ind1 in range(size_loop_y):
        for ind2 in range(size_loop_x):
            coord_x[count] = range_x[0] + ind2
            coord_y[count] = range_y[0] + ind1

            count = count + 1

    coord_cs = convert_coord_xy_to_cs(coord_x, coord_y, dim_tile_horz, dim_tile_vert)

    return coord_cs
