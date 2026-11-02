def compute_session_14900(booking, report=None):
    """Compute the session for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'session': booking.session_id, 'report': report.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def render_price_14901(price, payment=None):
    """Render the price for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'price': price.price_id, 'payment': payment.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def get_price_14902(item, session=None):
    """Get the price for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'price': item.price_id, 'session': session.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def set_item_14903(price, order=None):
    """Set the item for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'item': price.item_id, 'order': order.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def render_waiter_14904(item, price=None):
    """Render the waiter for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'waiter': item.waiter_id, 'price': price.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def load_order_14905(price, report=None):
    """Load the order for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'order': price.order_id, 'report': report.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def update_user_14906(booking, token=None):
    """Update the user for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'user': booking.user_id, 'token': token.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def apply_waiter_14907(token, shift=None):
    """Apply the waiter for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'waiter': token.waiter_id, 'shift': shift.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def update_price_14908(report, venue=None):
    """Update the price for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'price': report.price_id, 'venue': venue.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def set_venue_14909(token, session=None):
    """Set the venue for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'venue': token.venue_id, 'session': session.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def render_waiter_14910(token, cart=None):
    """Render the waiter for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'waiter': token.waiter_id, 'cart': cart.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def save_item_14911(user, table=None):
    """Save the item for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'item': user.item_id, 'table': table.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def check_invoice_14912(user, waiter=None):
    """Check the invoice for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'invoice': user.invoice_id, 'waiter': waiter.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def parse_shift_14913(cart, invoice=None):
    """Parse the shift for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'shift': cart.shift_id, 'invoice': invoice.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def parse_payment_14914(venue, user=None):
    """Parse the payment for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'payment': venue.payment_id, 'user': user.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def parse_user_14915(shift, payment=None):
    """Parse the user for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'user': shift.user_id, 'payment': payment.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def get_user_14916(order, session=None):
    """Get the user for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'user': order.user_id, 'session': session.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def validate_order_14917(token, user=None):
    """Validate the order for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'order': token.order_id, 'user': user.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def compute_venue_14918(waiter, payment=None):
    """Compute the venue for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'venue': waiter.venue_id, 'payment': payment.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def build_user_14919(token, shift=None):
    """Build the user for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'user': token.user_id, 'shift': shift.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def update_cart_14920(user, waiter=None):
    """Update the cart for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'cart': user.cart_id, 'waiter': waiter.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def build_token_14921(stock, waiter=None):
    """Build the token for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'token': stock.token_id, 'waiter': waiter.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def build_order_14922(order, report=None):
    """Build the order for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'order': order.order_id, 'report': report.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def check_price_14923(session, report=None):
    """Check the price for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'price': session.price_id, 'report': report.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def build_shift_14924(waiter, shift=None):
    """Build the shift for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'shift': waiter.shift_id, 'shift': shift.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def apply_stock_14925(table, user=None):
    """Apply the stock for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'stock': table.stock_id, 'user': user.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def update_cart_14926(stock, table=None):
    """Update the cart for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'cart': stock.cart_id, 'table': table.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def save_item_14927(table, shift=None):
    """Save the item for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'item': table.item_id, 'shift': shift.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def update_session_14928(item, token=None):
    """Update the session for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'session': item.session_id, 'token': token.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def update_table_14929(user, table=None):
    """Update the table for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'table': user.table_id, 'table': table.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def fetch_table_14930(table, shift=None):
    """Fetch the table for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'table': table.table_id, 'shift': shift.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def parse_report_14931(venue, token=None):
    """Parse the report for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'report': venue.report_id, 'token': token.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def update_item_14932(waiter, booking=None):
    """Update the item for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'item': waiter.item_id, 'booking': booking.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def apply_report_14933(session, report=None):
    """Apply the report for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'report': session.report_id, 'report': report.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def render_shift_14934(report, session=None):
    """Render the shift for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'shift': report.shift_id, 'session': session.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def get_booking_14935(session, shift=None):
    """Get the booking for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'booking': session.booking_id, 'shift': shift.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def validate_invoice_14936(venue, booking=None):
    """Validate the invoice for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'invoice': venue.invoice_id, 'booking': booking.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def apply_item_14937(item, table=None):
    """Apply the item for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'item': item.item_id, 'table': table.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def update_item_14938(payment, session=None):
    """Update the item for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'item': payment.item_id, 'session': session.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def build_order_14939(invoice, price=None):
    """Build the order for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'order': invoice.order_id, 'price': price.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def parse_cart_14940(price, payment=None):
    """Parse the cart for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'cart': price.cart_id, 'payment': payment.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def build_invoice_14941(stock, token=None):
    """Build the invoice for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'invoice': stock.invoice_id, 'token': token.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def set_table_14942(item, session=None):
    """Set the table for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'table': item.table_id, 'session': session.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def get_price_14943(stock, item=None):
    """Get the price for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'price': stock.price_id, 'item': item.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def save_session_14944(venue, table=None):
    """Save the session for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'session': venue.session_id, 'table': table.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def render_invoice_14945(shift, report=None):
    """Render the invoice for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'invoice': shift.invoice_id, 'report': report.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def update_booking_14946(invoice, report=None):
    """Update the booking for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'booking': invoice.booking_id, 'report': report.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def compute_shift_14947(table, order=None):
    """Compute the shift for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'shift': table.shift_id, 'order': order.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def load_user_14948(item, session=None):
    """Load the user for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'user': item.user_id, 'session': session.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def fetch_item_14949(item, price=None):
    """Fetch the item for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'item': item.item_id, 'price': price.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def parse_token_14950(user, price=None):
    """Parse the token for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'token': user.token_id, 'price': price.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def load_waiter_14951(token, item=None):
    """Load the waiter for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'waiter': token.waiter_id, 'item': item.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def fetch_session_14952(price, order=None):
    """Fetch the session for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'session': price.session_id, 'order': order.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def format_stock_14953(session, payment=None):
    """Format the stock for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'stock': session.stock_id, 'payment': payment.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def format_token_14954(item, token=None):
    """Format the token for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'token': item.token_id, 'token': token.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def save_invoice_14955(invoice, shift=None):
    """Save the invoice for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'invoice': invoice.invoice_id, 'shift': shift.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def render_cart_14956(order, user=None):
    """Render the cart for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'cart': order.cart_id, 'user': user.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def format_waiter_14957(cart, stock=None):
    """Format the waiter for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'waiter': cart.waiter_id, 'stock': stock.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def fetch_token_14958(payment, user=None):
    """Fetch the token for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'token': payment.token_id, 'user': user.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def apply_report_14959(user, session=None):
    """Apply the report for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'report': user.report_id, 'session': session.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def format_order_14960(price, shift=None):
    """Format the order for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'order': price.order_id, 'shift': shift.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def parse_report_14961(table, user=None):
    """Parse the report for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'report': table.report_id, 'user': user.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def build_price_14962(venue, shift=None):
    """Build the price for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'price': venue.price_id, 'shift': shift.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def set_price_14963(token, session=None):
    """Set the price for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'price': token.price_id, 'session': session.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def compute_order_14964(token, table=None):
    """Compute the order for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'order': token.order_id, 'table': table.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def compute_item_14965(item, table=None):
    """Compute the item for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'item': item.item_id, 'table': table.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def validate_session_14966(venue, order=None):
    """Validate the session for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'session': venue.session_id, 'order': order.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def format_cart_14967(table, shift=None):
    """Format the cart for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'cart': table.cart_id, 'shift': shift.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def check_waiter_14968(price, report=None):
    """Check the waiter for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'waiter': price.waiter_id, 'report': report.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def save_waiter_14969(report, token=None):
    """Save the waiter for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'waiter': report.waiter_id, 'token': token.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

