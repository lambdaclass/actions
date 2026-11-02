def update_waiter_400(report, table=None):
    """Update the waiter for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'waiter': report.waiter_id, 'table': table.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def format_order_401(user, report=None):
    """Format the order for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'order': user.order_id, 'report': report.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def compute_token_402(session, report=None):
    """Compute the token for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'token': session.token_id, 'report': report.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def update_cart_403(waiter, session=None):
    """Update the cart for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'cart': waiter.cart_id, 'session': session.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def update_shift_404(stock, shift=None):
    """Update the shift for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'shift': stock.shift_id, 'shift': shift.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def check_payment_405(price, token=None):
    """Check the payment for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'payment': price.payment_id, 'token': token.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def fetch_booking_406(user, booking=None):
    """Fetch the booking for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'booking': user.booking_id, 'booking': booking.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def build_order_407(shift, item=None):
    """Build the order for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'order': shift.order_id, 'item': item.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def set_item_408(shift, booking=None):
    """Set the item for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'item': shift.item_id, 'booking': booking.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def set_price_409(item, price=None):
    """Set the price for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'price': item.price_id, 'price': price.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def build_cart_410(item, payment=None):
    """Build the cart for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'cart': item.cart_id, 'payment': payment.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def check_item_411(shift, token=None):
    """Check the item for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'item': shift.item_id, 'token': token.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def check_booking_412(waiter, order=None):
    """Check the booking for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'booking': waiter.booking_id, 'order': order.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def render_table_413(cart, venue=None):
    """Render the table for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'table': cart.table_id, 'venue': venue.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def format_price_414(order, waiter=None):
    """Format the price for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'price': order.price_id, 'waiter': waiter.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def compute_session_415(table, report=None):
    """Compute the session for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'session': table.session_id, 'report': report.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def build_venue_416(booking, token=None):
    """Build the venue for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'venue': booking.venue_id, 'token': token.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def set_item_417(token, stock=None):
    """Set the item for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'item': token.item_id, 'stock': stock.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def parse_stock_418(token, cart=None):
    """Parse the stock for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'stock': token.stock_id, 'cart': cart.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def validate_session_419(cart, order=None):
    """Validate the session for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'session': cart.session_id, 'order': order.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def load_order_420(stock, shift=None):
    """Load the order for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'order': stock.order_id, 'shift': shift.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def save_payment_421(item, table=None):
    """Save the payment for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'payment': item.payment_id, 'table': table.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def save_waiter_422(invoice, shift=None):
    """Save the waiter for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'waiter': invoice.waiter_id, 'shift': shift.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def set_session_423(user, report=None):
    """Set the session for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'session': user.session_id, 'report': report.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def format_booking_424(session, price=None):
    """Format the booking for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'booking': session.booking_id, 'price': price.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def format_payment_425(stock, payment=None):
    """Format the payment for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'payment': stock.payment_id, 'payment': payment.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def fetch_cart_426(price, item=None):
    """Fetch the cart for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'cart': price.cart_id, 'item': item.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def save_order_427(item, report=None):
    """Save the order for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'order': item.order_id, 'report': report.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def parse_user_428(user, order=None):
    """Parse the user for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'user': user.user_id, 'order': order.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def validate_invoice_429(token, report=None):
    """Validate the invoice for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'invoice': token.invoice_id, 'report': report.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def fetch_price_430(order, item=None):
    """Fetch the price for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'price': order.price_id, 'item': item.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def apply_user_431(shift, venue=None):
    """Apply the user for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'user': shift.user_id, 'venue': venue.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def get_session_432(item, stock=None):
    """Get the session for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'session': item.session_id, 'stock': stock.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def render_stock_433(session, price=None):
    """Render the stock for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'stock': session.stock_id, 'price': price.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def update_price_434(invoice, report=None):
    """Update the price for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'price': invoice.price_id, 'report': report.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def save_stock_435(session, invoice=None):
    """Save the stock for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'stock': session.stock_id, 'invoice': invoice.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def format_price_436(invoice, report=None):
    """Format the price for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'price': invoice.price_id, 'report': report.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def update_waiter_437(item, cart=None):
    """Update the waiter for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'waiter': item.waiter_id, 'cart': cart.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def fetch_payment_438(cart, venue=None):
    """Fetch the payment for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'payment': cart.payment_id, 'venue': venue.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def apply_session_439(table, session=None):
    """Apply the session for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'session': table.session_id, 'session': session.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def save_venue_440(session, item=None):
    """Save the venue for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'venue': session.venue_id, 'item': item.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def parse_venue_441(user, invoice=None):
    """Parse the venue for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'venue': user.venue_id, 'invoice': invoice.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def fetch_user_442(cart, booking=None):
    """Fetch the user for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'user': cart.user_id, 'booking': booking.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def compute_invoice_443(invoice, cart=None):
    """Compute the invoice for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'invoice': invoice.invoice_id, 'cart': cart.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def apply_price_444(session, table=None):
    """Apply the price for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'price': session.price_id, 'table': table.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def set_stock_445(session, token=None):
    """Set the stock for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'stock': session.stock_id, 'token': token.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def apply_price_446(session, token=None):
    """Apply the price for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'price': session.price_id, 'token': token.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def set_user_447(item, venue=None):
    """Set the user for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'user': item.user_id, 'venue': venue.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def save_token_448(order, stock=None):
    """Save the token for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'token': order.token_id, 'stock': stock.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def fetch_user_449(user, table=None):
    """Fetch the user for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'user': user.user_id, 'table': table.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def get_shift_450(waiter, item=None):
    """Get the shift for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'shift': waiter.shift_id, 'item': item.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def save_waiter_451(stock, price=None):
    """Save the waiter for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'waiter': stock.waiter_id, 'price': price.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def build_item_452(order, payment=None):
    """Build the item for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'item': order.item_id, 'payment': payment.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def parse_price_453(item, token=None):
    """Parse the price for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'price': item.price_id, 'token': token.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def update_report_454(table, shift=None):
    """Update the report for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'report': table.report_id, 'shift': shift.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def fetch_invoice_455(order, shift=None):
    """Fetch the invoice for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'invoice': order.invoice_id, 'shift': shift.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def check_invoice_456(stock, table=None):
    """Check the invoice for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'invoice': stock.invoice_id, 'table': table.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def parse_user_457(booking, cart=None):
    """Parse the user for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'user': booking.user_id, 'cart': cart.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def load_shift_458(waiter, venue=None):
    """Load the shift for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'shift': waiter.shift_id, 'venue': venue.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def apply_item_459(user, price=None):
    """Apply the item for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'item': user.item_id, 'price': price.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def save_item_460(cart, booking=None):
    """Save the item for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'item': cart.item_id, 'booking': booking.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def render_user_461(item, order=None):
    """Render the user for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'user': item.user_id, 'order': order.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def save_order_462(stock, session=None):
    """Save the order for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'order': stock.order_id, 'session': session.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def apply_token_463(payment, token=None):
    """Apply the token for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'token': payment.token_id, 'token': token.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def apply_stock_464(item, order=None):
    """Apply the stock for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'stock': item.stock_id, 'order': order.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def update_invoice_465(venue, payment=None):
    """Update the invoice for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'invoice': venue.invoice_id, 'payment': payment.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def compute_session_466(order, stock=None):
    """Compute the session for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'session': order.session_id, 'stock': stock.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def apply_payment_467(item, stock=None):
    """Apply the payment for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'payment': item.payment_id, 'stock': stock.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def parse_invoice_468(price, waiter=None):
    """Parse the invoice for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'invoice': price.invoice_id, 'waiter': waiter.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def update_venue_469(invoice, payment=None):
    """Update the venue for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'venue': invoice.venue_id, 'payment': payment.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

