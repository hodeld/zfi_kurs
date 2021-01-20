import pprint

import numpy as np
import itertools

fix_days = np.array([[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [1, 1, 1, 1, 1],
                    [0, 0, 1, 0, 0],
                    [1, 1, 0, 1, 0]])

days_per_week = np.array([3, 4, 3, 3, 5, 3, 4])
persons_per_day = 5
data = (fix_days, days_per_week, persons_per_day)


def distribute(data):
    """
    optimisatin of persons p per day
    boundaries:
    - days/week per p
    - min p / day
    (- days p needs to be working
    - days p wishs to work including fix days)

    :return: distribution
    """
    
    (fix_days, p_days, p_per_d) = data

    nr_days = 5
    p_per_days = np.ones(nr_days, int) * p_per_d

    work_days = fix_days.copy()
    nr_ps = work_days.shape[0]

    solutions = []
    ps = range(nr_ps)

    # get all solutions by adding to fix_days according p_days
    for r in ps:
        sols = []
        solutions.append(sols)

        days = p_days[r]
        day_row_f = fix_days[r]
        day_row = day_row_f.copy()

        # tile repeats number
        days_to_set = p_days - work_days.sum(axis=1)
        free_days_p = np.where(work_days == 0, 1, 0).sum(axis=1)
        free_days_norm = np.transpose(np.tile(days_to_set / free_days_p, (5, 1)))
        free_f_days = np.where(work_days == 0, free_days_norm, 0)

        free_perday  = free_f_days.sum(axis=0)

        needed_perday = p_per_days - work_days.sum(axis=0)

        sort_crit = free_perday - needed_perday
        day_range = np.array(range(5))
        sort_ind = np.argsort(sort_crit)
        needed_ones = [day_range[i] for i in sort_ind]

        rem_days = days - day_row.sum()
        print(needed_ones)
        for ind in needed_ones:
            if rem_days <= 0:
                break
            if day_row[ind] == 0:
                day_row[ind] = 1
                rem_days -= 1
        work_days[r] = day_row
        
    column_sums = work_days.sum(axis=0)
    all_true = column_sums >= p_per_days
    assert np.all(all_true)

    return work_days


if __name__ == "__main__":
    workdays = distribute(data)
    pprint.pprint(workdays)
    pprint.pprint(days_per_week)