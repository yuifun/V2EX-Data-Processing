import getting_topic_id
import option
import settings


def main():
    args = option.Parse()
    config = settings.Read(args['config'])

    getting_topic_id.get(1, 20, config['cookie'])


if __name__ == '__main__':
    main()
