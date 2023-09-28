def ft_statistics(*args: any, **kwargs: any) -> None:
    """Print the required statistical values of the args list"""

    for num in args:
        if not (isinstance(num, (float, int)) and not isinstance(num, bool)):
            print('args contains invalid values')
            return

    length = len(args)
    nums = sorted(args)
    mid = length // 2
    if length != 0:  # prevent division by 0 error
        mean = sum(nums) / length
        var = sum((num - mean) ** 2 for num in nums) / length
    for _, measure in kwargs.items():
        if measure not in ['mean', 'median', 'quartile', 'std', 'var']:
            continue

        if length == 0:
            print('ERROR')

        elif measure == 'mean':
            print('mean :', mean)

        elif measure == 'median':
            if length % 2 != 0:
                median = nums[mid]
            else:
                median = (nums[mid] + nums[mid + 1]) / 2
            print('median :', median)

        elif measure == 'quartile':
            q1 = float(nums[mid - mid // 2])
            q3 = float(nums[mid + mid // 2])
            quartiles = [q1, q3]
            print('quartile :', quartiles)

        elif measure == 'std':
            std = var ** 0.5
            print('std :', std)

        elif measure == 'var':
            mean = sum(nums) / length
            print('var :', var)
