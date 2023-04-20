from producer import connect_kafka_producer, get_recipes, publish_message


if __name__ == '__main__':

    all_recipes = get_recipes()
    if len(all_recipes) > 0:
        kafka_producer = connect_kafka_producer()
    for recipe in all_recipes:
        publish_message(kafka_producer, 'raw_recipes', 'raw', recipe.strip())
        if kafka_producer is not None:
            kafka_producer.close()
