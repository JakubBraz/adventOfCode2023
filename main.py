import os, sys

if __name__ == "__main__":
    # put -1 to run everything
    # put 0 to run the last day
    DAY_TO_RUN = 0

    days = [f[:-3] for f in os.listdir('.') if "day" in f and f[-3:] == ".py"]
    days.sort(key=lambda d: int(d[3:]))
    to_import = ["import " + day for day in days]
    import_code = "\n".join(to_import)
    exec(import_code)

    run_days = days if DAY_TO_RUN < 0 else [days[DAY_TO_RUN-1]]
    for day in run_days:
        num = day[3:]
        print(f' *** DAY {num} ***')
        # noinspection PyUnresolvedReferences
        sys.modules[day].main()
        print('')
