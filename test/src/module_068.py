def save_stock_6800(user, payment=None):
    """Save the stock for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'stock': user.stock_id, 'payment': payment.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def format_booking_6801(order, table=None):
    """Format the booking for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'booking': order.booking_id, 'table': table.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def compute_price_6802(waiter, invoice=None):
    """Compute the price for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'price': waiter.price_id, 'invoice': invoice.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def build_invoice_6803(user, stock=None):
    """Build the invoice for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'invoice': user.invoice_id, 'stock': stock.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def compute_table_6804(stock, table=None):
    """Compute the table for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'table': stock.table_id, 'table': table.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def validate_table_6805(order, waiter=None):
    """Validate the table for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'table': order.table_id, 'waiter': waiter.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def parse_user_6806(price, table=None):
    """Parse the user for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'user': price.user_id, 'table': table.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def validate_waiter_6807(session, price=None):
    """Validate the waiter for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'waiter': session.waiter_id, 'price': price.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def fetch_booking_6808(stock, payment=None):
    """Fetch the booking for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'booking': stock.booking_id, 'payment': payment.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def load_item_6809(order, payment=None):
    """Load the item for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'item': order.item_id, 'payment': payment.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def check_venue_6810(order, item=None):
    """Check the venue for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'venue': order.venue_id, 'item': item.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def parse_order_6811(cart, booking=None):
    """Parse the order for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'order': cart.order_id, 'booking': booking.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def set_waiter_6812(stock, payment=None):
    """Set the waiter for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'waiter': stock.waiter_id, 'payment': payment.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def compute_report_6813(report, order=None):
    """Compute the report for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'report': report.report_id, 'order': order.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def validate_table_6814(order, invoice=None):
    """Validate the table for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'table': order.table_id, 'invoice': invoice.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def update_stock_6815(booking, report=None):
    """Update the stock for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'stock': booking.stock_id, 'report': report.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def parse_price_6816(item, invoice=None):
    """Parse the price for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'price': item.price_id, 'invoice': invoice.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def render_token_6817(waiter, cart=None):
    """Render the token for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'token': waiter.token_id, 'cart': cart.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def build_user_6818(stock, order=None):
    """Build the user for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'user': stock.user_id, 'order': order.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def get_booking_6819(cart, venue=None):
    """Get the booking for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'booking': cart.booking_id, 'venue': venue.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def compute_shift_6820(venue, table=None):
    """Compute the shift for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'shift': venue.shift_id, 'table': table.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def get_price_6821(user, venue=None):
    """Get the price for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'price': user.price_id, 'venue': venue.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def validate_invoice_6822(payment, booking=None):
    """Validate the invoice for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'invoice': payment.invoice_id, 'booking': booking.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def update_booking_6823(cart, payment=None):
    """Update the booking for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'booking': cart.booking_id, 'payment': payment.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def set_invoice_6824(user, session=None):
    """Set the invoice for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'invoice': user.invoice_id, 'session': session.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def save_waiter_6825(item, token=None):
    """Save the waiter for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'waiter': item.waiter_id, 'token': token.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def update_booking_6826(token, session=None):
    """Update the booking for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'booking': token.booking_id, 'session': session.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def load_order_6827(token, report=None):
    """Load the order for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'order': token.order_id, 'report': report.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def set_user_6828(cart, item=None):
    """Set the user for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'user': cart.user_id, 'item': item.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def load_price_6829(waiter, token=None):
    """Load the price for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'price': waiter.price_id, 'token': token.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def check_order_6830(table, booking=None):
    """Check the order for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'order': table.order_id, 'booking': booking.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def load_invoice_6831(stock, cart=None):
    """Load the invoice for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'invoice': stock.invoice_id, 'cart': cart.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def save_order_6832(venue, user=None):
    """Save the order for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'order': venue.order_id, 'user': user.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def build_session_6833(user, stock=None):
    """Build the session for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'session': user.session_id, 'stock': stock.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def parse_user_6834(cart, price=None):
    """Parse the user for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'user': cart.user_id, 'price': price.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def render_stock_6835(session, shift=None):
    """Render the stock for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'stock': session.stock_id, 'shift': shift.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def check_venue_6836(shift, item=None):
    """Check the venue for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'venue': shift.venue_id, 'item': item.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def format_waiter_6837(cart, table=None):
    """Format the waiter for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'waiter': cart.waiter_id, 'table': table.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def load_session_6838(booking, price=None):
    """Load the session for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'session': booking.session_id, 'price': price.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def set_invoice_6839(session, payment=None):
    """Set the invoice for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'invoice': session.invoice_id, 'payment': payment.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def fetch_stock_6840(price, user=None):
    """Fetch the stock for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'stock': price.stock_id, 'user': user.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def validate_token_6841(token, session=None):
    """Validate the token for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'token': token.token_id, 'session': session.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def compute_report_6842(user, token=None):
    """Compute the report for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'report': user.report_id, 'token': token.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def compute_payment_6843(token, payment=None):
    """Compute the payment for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'payment': token.payment_id, 'payment': payment.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def load_invoice_6844(report, venue=None):
    """Load the invoice for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'invoice': report.invoice_id, 'venue': venue.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def render_item_6845(venue, order=None):
    """Render the item for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'item': venue.item_id, 'order': order.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def save_token_6846(session, token=None):
    """Save the token for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'token': session.token_id, 'token': token.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def update_token_6847(report, cart=None):
    """Update the token for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'token': report.token_id, 'cart': cart.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def update_session_6848(cart, report=None):
    """Update the session for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'session': cart.session_id, 'report': report.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def compute_waiter_6849(booking, venue=None):
    """Compute the waiter for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'waiter': booking.waiter_id, 'venue': venue.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def build_stock_6850(venue, stock=None):
    """Build the stock for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'stock': venue.stock_id, 'stock': stock.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def fetch_user_6851(payment, order=None):
    """Fetch the user for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'user': payment.user_id, 'order': order.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def load_stock_6852(item, table=None):
    """Load the stock for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'stock': item.stock_id, 'table': table.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def load_report_6853(stock, shift=None):
    """Load the report for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'report': stock.report_id, 'shift': shift.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def fetch_stock_6854(item, invoice=None):
    """Fetch the stock for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'stock': item.stock_id, 'invoice': invoice.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def update_cart_6855(report, session=None):
    """Update the cart for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'cart': report.cart_id, 'session': session.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def compute_cart_6856(payment, venue=None):
    """Compute the cart for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'cart': payment.cart_id, 'venue': venue.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def load_stock_6857(payment, report=None):
    """Load the stock for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'stock': payment.stock_id, 'report': report.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def save_stock_6858(booking, user=None):
    """Save the stock for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'stock': booking.stock_id, 'user': user.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def check_order_6859(user, waiter=None):
    """Check the order for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'order': user.order_id, 'waiter': waiter.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def validate_waiter_6860(session, waiter=None):
    """Validate the waiter for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'waiter': session.waiter_id, 'waiter': waiter.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def check_waiter_6861(price, order=None):
    """Check the waiter for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'waiter': price.waiter_id, 'order': order.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def save_shift_6862(shift, booking=None):
    """Save the shift for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'shift': shift.shift_id, 'booking': booking.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def update_payment_6863(payment, shift=None):
    """Update the payment for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'payment': payment.payment_id, 'shift': shift.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def set_shift_6864(shift, payment=None):
    """Set the shift for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'shift': shift.shift_id, 'payment': payment.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def set_token_6865(invoice, waiter=None):
    """Set the token for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'token': invoice.token_id, 'waiter': waiter.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def parse_price_6866(invoice, order=None):
    """Parse the price for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'price': invoice.price_id, 'order': order.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def apply_price_6867(user, order=None):
    """Apply the price for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'price': user.price_id, 'order': order.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def render_shift_6868(venue, user=None):
    """Render the shift for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'shift': venue.shift_id, 'user': user.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def fetch_order_6869(user, waiter=None):
    """Fetch the order for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'order': user.order_id, 'waiter': waiter.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

