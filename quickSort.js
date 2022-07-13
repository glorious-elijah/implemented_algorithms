const quickSort = (list, rev = false) => {
  if (list.length <= 1) {
    return list;
  }
  let great = [];
  let less = [];
  const PIVOT = list[0];

  for (let i = 1; i < list.length; i++) {
    if (list[i] <= PIVOT) {
      less.push(list[i]);
    } else {
      great.push(list[i]);
    }
  }
  if (rev) {
    return quickSort(great, rev) + " " + [PIVOT] + " " + quickSort(less, rev);
  } else {
    return quickSort(less, rev) + " " + [PIVOT] + " " + quickSort(great, rev);
  }
};
