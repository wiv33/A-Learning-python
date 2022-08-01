def main_run():
    from music21 import converter

    dataset_name = 'cello'
    filename = 'cs1-2all'
    file = "./data/{}/{}.mid".format(dataset_name, filename)

    original_score = converter.parse(file).chordify()
    original_score.show('text')


if __name__ == '__main__':
    main_run()
