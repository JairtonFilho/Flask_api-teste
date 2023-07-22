from flask import request, url_for


def paginate(model, schema):
    page: int = int(request.args.get('page', 1))
    per_page: int = int(request.args.get('per_page', 10))
    paginated = model.query.paginate(page=page, per_page=per_page)

    next = url_for(
        request.endpoint,
        page=paginated.next_num if paginated.has_next else paginated.page, per_page=per_page, **request.view_args
    )

    prev = url_for(
        request.endpoint,
        page=paginated.prev_num if paginated.has_prev else paginated.page, per_page=per_page, **request.view_args
    )

    return {
        'total': paginated.total,
        'pages': paginated.pages,
        'next': next,
        'prev': prev,
        'results': schema.dump(paginated.items)
    }
