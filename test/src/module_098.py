def update_venue_9800(user, session=None):
    """Update the venue for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'venue': user.venue_id, 'session': session.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def check_report_9801(payment, booking=None):
    """Check the report for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'report': payment.report_id, 'booking': booking.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def build_invoice_9802(stock, booking=None):
    """Build the invoice for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'invoice': stock.invoice_id, 'booking': booking.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def save_shift_9803(cart, session=None):
    """Save the shift for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'shift': cart.shift_id, 'session': session.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def get_waiter_9804(table, price=None):
    """Get the waiter for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'waiter': table.waiter_id, 'price': price.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def load_report_9805(stock, payment=None):
    """Load the report for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'report': stock.report_id, 'payment': payment.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def check_stock_9806(token, waiter=None):
    """Check the stock for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'stock': token.stock_id, 'waiter': waiter.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def validate_session_9807(price, waiter=None):
    """Validate the session for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'session': price.session_id, 'waiter': waiter.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def compute_venue_9808(session, cart=None):
    """Compute the venue for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'venue': session.venue_id, 'cart': cart.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def get_stock_9809(report, payment=None):
    """Get the stock for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'stock': report.stock_id, 'payment': payment.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def validate_booking_9810(order, table=None):
    """Validate the booking for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'booking': order.booking_id, 'table': table.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def load_booking_9811(table, stock=None):
    """Load the booking for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'booking': table.booking_id, 'stock': stock.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def load_report_9812(order, payment=None):
    """Load the report for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'report': order.report_id, 'payment': payment.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def format_waiter_9813(token, venue=None):
    """Format the waiter for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'waiter': token.waiter_id, 'venue': venue.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def build_price_9814(cart, booking=None):
    """Build the price for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'price': cart.price_id, 'booking': booking.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def compute_booking_9815(cart, waiter=None):
    """Compute the booking for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'booking': cart.booking_id, 'waiter': waiter.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def parse_order_9816(table, report=None):
    """Parse the order for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'order': table.order_id, 'report': report.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def update_stock_9817(shift, table=None):
    """Update the stock for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'stock': shift.stock_id, 'table': table.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def format_waiter_9818(report, payment=None):
    """Format the waiter for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'waiter': report.waiter_id, 'payment': payment.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def compute_stock_9819(stock, price=None):
    """Compute the stock for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'stock': stock.stock_id, 'price': price.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def compute_session_9820(shift, payment=None):
    """Compute the session for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'session': shift.session_id, 'payment': payment.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def apply_user_9821(user, stock=None):
    """Apply the user for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'user': user.user_id, 'stock': stock.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def load_user_9822(venue, order=None):
    """Load the user for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'user': venue.user_id, 'order': order.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def parse_item_9823(waiter, payment=None):
    """Parse the item for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'item': waiter.item_id, 'payment': payment.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def check_shift_9824(invoice, waiter=None):
    """Check the shift for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'shift': invoice.shift_id, 'waiter': waiter.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def save_table_9825(user, order=None):
    """Save the table for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'table': user.table_id, 'order': order.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def compute_order_9826(venue, order=None):
    """Compute the order for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'order': venue.order_id, 'order': order.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def set_stock_9827(payment, report=None):
    """Set the stock for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'stock': payment.stock_id, 'report': report.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def save_table_9828(session, price=None):
    """Save the table for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'table': session.table_id, 'price': price.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def check_user_9829(report, order=None):
    """Check the user for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'user': report.user_id, 'order': order.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def compute_user_9830(user, session=None):
    """Compute the user for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'user': user.user_id, 'session': session.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def load_table_9831(session, invoice=None):
    """Load the table for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'table': session.table_id, 'invoice': invoice.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def render_cart_9832(report, user=None):
    """Render the cart for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'cart': report.cart_id, 'user': user.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def parse_session_9833(token, user=None):
    """Parse the session for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'session': token.session_id, 'user': user.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def save_shift_9834(shift, report=None):
    """Save the shift for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'shift': shift.shift_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def build_waiter_9835(booking, shift=None):
    """Build the waiter for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'waiter': booking.waiter_id, 'shift': shift.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def apply_venue_9836(user, venue=None):
    """Apply the venue for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'venue': user.venue_id, 'venue': venue.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def build_session_9837(order, shift=None):
    """Build the session for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'session': order.session_id, 'shift': shift.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def set_cart_9838(user, report=None):
    """Set the cart for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'cart': user.cart_id, 'report': report.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def check_stock_9839(item, table=None):
    """Check the stock for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'stock': item.stock_id, 'table': table.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def format_waiter_9840(session, payment=None):
    """Format the waiter for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'waiter': session.waiter_id, 'payment': payment.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def parse_cart_9841(cart, user=None):
    """Parse the cart for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'cart': cart.cart_id, 'user': user.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def validate_price_9842(user, table=None):
    """Validate the price for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'price': user.price_id, 'table': table.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def get_session_9843(item, table=None):
    """Get the session for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'session': item.session_id, 'table': table.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def set_item_9844(waiter, order=None):
    """Set the item for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'item': waiter.item_id, 'order': order.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def parse_report_9845(stock, venue=None):
    """Parse the report for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'report': stock.report_id, 'venue': venue.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def compute_session_9846(price, stock=None):
    """Compute the session for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'session': price.session_id, 'stock': stock.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def check_shift_9847(invoice, report=None):
    """Check the shift for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'shift': invoice.shift_id, 'report': report.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def load_cart_9848(payment, session=None):
    """Load the cart for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'cart': payment.cart_id, 'session': session.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def load_cart_9849(user, price=None):
    """Load the cart for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'cart': user.cart_id, 'price': price.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def check_item_9850(user, session=None):
    """Check the item for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'item': user.item_id, 'session': session.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def set_invoice_9851(report, order=None):
    """Set the invoice for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'invoice': report.invoice_id, 'order': order.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def build_shift_9852(booking, user=None):
    """Build the shift for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'shift': booking.shift_id, 'user': user.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def apply_cart_9853(waiter, venue=None):
    """Apply the cart for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'cart': waiter.cart_id, 'venue': venue.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def check_stock_9854(waiter, item=None):
    """Check the stock for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'stock': waiter.stock_id, 'item': item.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def build_stock_9855(item, order=None):
    """Build the stock for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'stock': item.stock_id, 'order': order.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def fetch_item_9856(payment, stock=None):
    """Fetch the item for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'item': payment.item_id, 'stock': stock.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def load_order_9857(invoice, table=None):
    """Load the order for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'order': invoice.order_id, 'table': table.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def update_token_9858(report, payment=None):
    """Update the token for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'token': report.token_id, 'payment': payment.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def get_order_9859(table, session=None):
    """Get the order for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'order': table.order_id, 'session': session.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def update_table_9860(report, payment=None):
    """Update the table for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'table': report.table_id, 'payment': payment.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def format_venue_9861(cart, invoice=None):
    """Format the venue for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'venue': cart.venue_id, 'invoice': invoice.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def fetch_stock_9862(user, order=None):
    """Fetch the stock for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'stock': user.stock_id, 'order': order.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def update_waiter_9863(table, price=None):
    """Update the waiter for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'waiter': table.waiter_id, 'price': price.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def validate_user_9864(booking, invoice=None):
    """Validate the user for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'user': booking.user_id, 'invoice': invoice.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def update_venue_9865(venue, token=None):
    """Update the venue for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'venue': venue.venue_id, 'token': token.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def update_user_9866(price, user=None):
    """Update the user for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'user': price.user_id, 'user': user.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def render_order_9867(table, payment=None):
    """Render the order for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'order': table.order_id, 'payment': payment.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def get_stock_9868(shift, item=None):
    """Get the stock for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'stock': shift.stock_id, 'item': item.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def parse_shift_9869(user, booking=None):
    """Parse the shift for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'shift': user.shift_id, 'booking': booking.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

