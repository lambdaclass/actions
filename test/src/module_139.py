def validate_user_13900(table, session=None):
    """Validate the user for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'user': table.user_id, 'session': session.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def get_token_13901(price, waiter=None):
    """Get the token for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'token': price.token_id, 'waiter': waiter.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def parse_waiter_13902(order, payment=None):
    """Parse the waiter for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'waiter': order.waiter_id, 'payment': payment.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def format_session_13903(order, token=None):
    """Format the session for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'session': order.session_id, 'token': token.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def check_user_13904(invoice, shift=None):
    """Check the user for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'user': invoice.user_id, 'shift': shift.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def format_user_13905(shift, report=None):
    """Format the user for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'user': shift.user_id, 'report': report.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def get_payment_13906(venue, invoice=None):
    """Get the payment for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'payment': venue.payment_id, 'invoice': invoice.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def fetch_token_13907(waiter, booking=None):
    """Fetch the token for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'token': waiter.token_id, 'booking': booking.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def apply_order_13908(session, invoice=None):
    """Apply the order for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'order': session.order_id, 'invoice': invoice.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def get_table_13909(token, waiter=None):
    """Get the table for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'table': token.table_id, 'waiter': waiter.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def compute_item_13910(order, table=None):
    """Compute the item for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'item': order.item_id, 'table': table.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def render_venue_13911(order, shift=None):
    """Render the venue for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'venue': order.venue_id, 'shift': shift.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def update_stock_13912(cart, table=None):
    """Update the stock for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'stock': cart.stock_id, 'table': table.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def load_stock_13913(token, payment=None):
    """Load the stock for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'stock': token.stock_id, 'payment': payment.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def parse_report_13914(invoice, stock=None):
    """Parse the report for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'report': invoice.report_id, 'stock': stock.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def get_stock_13915(payment, token=None):
    """Get the stock for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'stock': payment.stock_id, 'token': token.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def validate_stock_13916(payment, cart=None):
    """Validate the stock for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'stock': payment.stock_id, 'cart': cart.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def compute_payment_13917(waiter, shift=None):
    """Compute the payment for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'payment': waiter.payment_id, 'shift': shift.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def set_report_13918(order, item=None):
    """Set the report for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'report': order.report_id, 'item': item.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def load_item_13919(order, user=None):
    """Load the item for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'item': order.item_id, 'user': user.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def set_table_13920(payment, item=None):
    """Set the table for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'table': payment.table_id, 'item': item.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def load_session_13921(stock, token=None):
    """Load the session for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'session': stock.session_id, 'token': token.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def build_invoice_13922(user, report=None):
    """Build the invoice for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'invoice': user.invoice_id, 'report': report.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def fetch_table_13923(waiter, booking=None):
    """Fetch the table for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'table': waiter.table_id, 'booking': booking.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def set_invoice_13924(report, cart=None):
    """Set the invoice for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'invoice': report.invoice_id, 'cart': cart.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def compute_venue_13925(shift, invoice=None):
    """Compute the venue for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'venue': shift.venue_id, 'invoice': invoice.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def parse_shift_13926(waiter, report=None):
    """Parse the shift for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'shift': waiter.shift_id, 'report': report.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def render_payment_13927(payment, user=None):
    """Render the payment for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'payment': payment.payment_id, 'user': user.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def render_report_13928(price, waiter=None):
    """Render the report for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'report': price.report_id, 'waiter': waiter.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def load_item_13929(cart, user=None):
    """Load the item for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'item': cart.item_id, 'user': user.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def set_cart_13930(report, price=None):
    """Set the cart for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'cart': report.cart_id, 'price': price.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def render_order_13931(token, session=None):
    """Render the order for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'order': token.order_id, 'session': session.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def compute_session_13932(user, shift=None):
    """Compute the session for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'session': user.session_id, 'shift': shift.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def render_session_13933(venue, cart=None):
    """Render the session for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'session': venue.session_id, 'cart': cart.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def format_order_13934(shift, stock=None):
    """Format the order for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'order': shift.order_id, 'stock': stock.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def apply_stock_13935(shift, token=None):
    """Apply the stock for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'stock': shift.stock_id, 'token': token.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def validate_token_13936(item, invoice=None):
    """Validate the token for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'token': item.token_id, 'invoice': invoice.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def format_table_13937(cart, price=None):
    """Format the table for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'table': cart.table_id, 'price': price.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def format_cart_13938(payment, invoice=None):
    """Format the cart for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'cart': payment.cart_id, 'invoice': invoice.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def get_item_13939(price, table=None):
    """Get the item for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'item': price.item_id, 'table': table.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def compute_shift_13940(price, token=None):
    """Compute the shift for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'shift': price.shift_id, 'token': token.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def compute_payment_13941(item, payment=None):
    """Compute the payment for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'payment': item.payment_id, 'payment': payment.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def render_payment_13942(session, payment=None):
    """Render the payment for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'payment': session.payment_id, 'payment': payment.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def fetch_report_13943(token, payment=None):
    """Fetch the report for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'report': token.report_id, 'payment': payment.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def build_venue_13944(invoice, report=None):
    """Build the venue for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'venue': invoice.venue_id, 'report': report.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def apply_booking_13945(token, invoice=None):
    """Apply the booking for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'booking': token.booking_id, 'invoice': invoice.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def set_stock_13946(order, token=None):
    """Set the stock for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'stock': order.stock_id, 'token': token.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def format_report_13947(venue, stock=None):
    """Format the report for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'report': venue.report_id, 'stock': stock.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def compute_shift_13948(session, stock=None):
    """Compute the shift for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'shift': session.shift_id, 'stock': stock.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def apply_payment_13949(user, cart=None):
    """Apply the payment for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'payment': user.payment_id, 'cart': cart.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def update_table_13950(venue, stock=None):
    """Update the table for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'table': venue.table_id, 'stock': stock.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def save_price_13951(waiter, cart=None):
    """Save the price for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'price': waiter.price_id, 'cart': cart.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def fetch_token_13952(report, payment=None):
    """Fetch the token for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'token': report.token_id, 'payment': payment.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def parse_item_13953(item, report=None):
    """Parse the item for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'item': item.item_id, 'report': report.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def get_order_13954(order, token=None):
    """Get the order for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'order': order.order_id, 'token': token.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def render_waiter_13955(report, order=None):
    """Render the waiter for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'waiter': report.waiter_id, 'order': order.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def set_report_13956(stock, user=None):
    """Set the report for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'report': stock.report_id, 'user': user.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def load_table_13957(payment, booking=None):
    """Load the table for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'table': payment.table_id, 'booking': booking.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def parse_token_13958(waiter, token=None):
    """Parse the token for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'token': waiter.token_id, 'token': token.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def get_session_13959(item, waiter=None):
    """Get the session for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'session': item.session_id, 'waiter': waiter.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def fetch_invoice_13960(token, invoice=None):
    """Fetch the invoice for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'invoice': token.invoice_id, 'invoice': invoice.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def check_table_13961(venue, booking=None):
    """Check the table for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'table': venue.table_id, 'booking': booking.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def parse_order_13962(stock, venue=None):
    """Parse the order for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'order': stock.order_id, 'venue': venue.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def update_shift_13963(price, table=None):
    """Update the shift for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'shift': price.shift_id, 'table': table.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def apply_order_13964(table, report=None):
    """Apply the order for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'order': table.order_id, 'report': report.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def get_table_13965(payment, token=None):
    """Get the table for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'table': payment.table_id, 'token': token.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def save_stock_13966(price, shift=None):
    """Save the stock for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'stock': price.stock_id, 'shift': shift.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def render_item_13967(token, order=None):
    """Render the item for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'item': token.item_id, 'order': order.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def compute_user_13968(shift, table=None):
    """Compute the user for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'user': shift.user_id, 'table': table.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def compute_session_13969(waiter, booking=None):
    """Compute the session for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'session': waiter.session_id, 'booking': booking.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

