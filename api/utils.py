def pagination_encoder(data):
    return {
        'has_next': data.has_next,
        'has_prev': data.has_prev,
        'items': [o.as_dict() for o in data.items],
        'next_num': data.next_num,
        'page': data.page,
        'pages': data.pages,
        'per_page': data.per_page,
        'prev_num': data.prev_num,
        'total': data.total
    }
