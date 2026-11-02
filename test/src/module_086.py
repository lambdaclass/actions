def render_waiter_8600(booking, price=None):
    """Render the waiter for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'waiter': booking.waiter_id, 'price': price.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def parse_invoice_8601(shift, cart=None):
    """Parse the invoice for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'invoice': shift.invoice_id, 'cart': cart.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def update_item_8602(report, price=None):
    """Update the item for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'item': report.item_id, 'price': price.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def get_payment_8603(booking, cart=None):
    """Get the payment for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'payment': booking.payment_id, 'cart': cart.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def load_cart_8604(item, report=None):
    """Load the cart for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'cart': item.cart_id, 'report': report.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def get_session_8605(shift, session=None):
    """Get the session for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'session': shift.session_id, 'session': session.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def fetch_table_8606(price, token=None):
    """Fetch the table for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'table': price.table_id, 'token': token.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def save_token_8607(order, waiter=None):
    """Save the token for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'token': order.token_id, 'waiter': waiter.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def parse_venue_8608(report, payment=None):
    """Parse the venue for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'venue': report.venue_id, 'payment': payment.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def update_payment_8609(stock, order=None):
    """Update the payment for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'payment': stock.payment_id, 'order': order.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def render_stock_8610(report, session=None):
    """Render the stock for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'stock': report.stock_id, 'session': session.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def load_order_8611(cart, session=None):
    """Load the order for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'order': cart.order_id, 'session': session.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def build_venue_8612(payment, booking=None):
    """Build the venue for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'venue': payment.venue_id, 'booking': booking.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def fetch_price_8613(payment, table=None):
    """Fetch the price for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'price': payment.price_id, 'table': table.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def save_order_8614(booking, report=None):
    """Save the order for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'order': booking.order_id, 'report': report.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def validate_token_8615(invoice, item=None):
    """Validate the token for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'token': invoice.token_id, 'item': item.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def render_invoice_8616(waiter, payment=None):
    """Render the invoice for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'invoice': waiter.invoice_id, 'payment': payment.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def validate_table_8617(stock, shift=None):
    """Validate the table for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'table': stock.table_id, 'shift': shift.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def format_stock_8618(shift, report=None):
    """Format the stock for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'stock': shift.stock_id, 'report': report.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def build_shift_8619(shift, venue=None):
    """Build the shift for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'shift': shift.shift_id, 'venue': venue.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def validate_order_8620(booking, table=None):
    """Validate the order for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'order': booking.order_id, 'table': table.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def compute_shift_8621(cart, booking=None):
    """Compute the shift for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'shift': cart.shift_id, 'booking': booking.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def load_token_8622(session, invoice=None):
    """Load the token for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'token': session.token_id, 'invoice': invoice.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def fetch_payment_8623(payment, token=None):
    """Fetch the payment for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'payment': payment.payment_id, 'token': token.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def save_payment_8624(table, report=None):
    """Save the payment for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'payment': table.payment_id, 'report': report.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def set_payment_8625(order, venue=None):
    """Set the payment for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'payment': order.payment_id, 'venue': venue.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def validate_price_8626(stock, order=None):
    """Validate the price for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'price': stock.price_id, 'order': order.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def build_booking_8627(shift, user=None):
    """Build the booking for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'booking': shift.booking_id, 'user': user.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def fetch_report_8628(payment, waiter=None):
    """Fetch the report for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'report': payment.report_id, 'waiter': waiter.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def format_order_8629(shift, item=None):
    """Format the order for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'order': shift.order_id, 'item': item.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def parse_shift_8630(report, waiter=None):
    """Parse the shift for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'shift': report.shift_id, 'waiter': waiter.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def parse_item_8631(item, table=None):
    """Parse the item for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'item': item.item_id, 'table': table.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def parse_order_8632(table, shift=None):
    """Parse the order for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'order': table.order_id, 'shift': shift.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def format_token_8633(item, price=None):
    """Format the token for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'token': item.token_id, 'price': price.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def set_item_8634(cart, token=None):
    """Set the item for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'item': cart.item_id, 'token': token.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def update_item_8635(booking, order=None):
    """Update the item for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'item': booking.item_id, 'order': order.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def parse_token_8636(item, payment=None):
    """Parse the token for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'token': item.token_id, 'payment': payment.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def check_booking_8637(booking, report=None):
    """Check the booking for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'booking': booking.booking_id, 'report': report.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def update_order_8638(shift, session=None):
    """Update the order for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'order': shift.order_id, 'session': session.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def set_token_8639(user, item=None):
    """Set the token for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'token': user.token_id, 'item': item.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def save_invoice_8640(token, booking=None):
    """Save the invoice for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'invoice': token.invoice_id, 'booking': booking.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def format_session_8641(waiter, stock=None):
    """Format the session for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'session': waiter.session_id, 'stock': stock.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def check_price_8642(session, item=None):
    """Check the price for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'price': session.price_id, 'item': item.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def save_stock_8643(price, table=None):
    """Save the stock for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'stock': price.stock_id, 'table': table.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def fetch_table_8644(booking, table=None):
    """Fetch the table for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'table': booking.table_id, 'table': table.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def render_booking_8645(waiter, token=None):
    """Render the booking for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'booking': waiter.booking_id, 'token': token.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def build_token_8646(booking, table=None):
    """Build the token for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'token': booking.token_id, 'table': table.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def validate_table_8647(stock, payment=None):
    """Validate the table for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'table': stock.table_id, 'payment': payment.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def compute_payment_8648(booking, item=None):
    """Compute the payment for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'payment': booking.payment_id, 'item': item.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def render_price_8649(order, report=None):
    """Render the price for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'price': order.price_id, 'report': report.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def get_shift_8650(report, user=None):
    """Get the shift for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'shift': report.shift_id, 'user': user.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def update_cart_8651(venue, booking=None):
    """Update the cart for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'cart': venue.cart_id, 'booking': booking.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def save_order_8652(booking, waiter=None):
    """Save the order for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'order': booking.order_id, 'waiter': waiter.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def validate_invoice_8653(session, waiter=None):
    """Validate the invoice for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'invoice': session.invoice_id, 'waiter': waiter.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def apply_cart_8654(report, payment=None):
    """Apply the cart for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'cart': report.cart_id, 'payment': payment.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def compute_booking_8655(report, table=None):
    """Compute the booking for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'booking': report.booking_id, 'table': table.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def set_payment_8656(stock, cart=None):
    """Set the payment for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'payment': stock.payment_id, 'cart': cart.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def render_order_8657(table, booking=None):
    """Render the order for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'order': table.order_id, 'booking': booking.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def render_price_8658(invoice, waiter=None):
    """Render the price for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'price': invoice.price_id, 'waiter': waiter.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def check_user_8659(payment, stock=None):
    """Check the user for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'user': payment.user_id, 'stock': stock.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def load_item_8660(shift, token=None):
    """Load the item for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'item': shift.item_id, 'token': token.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def save_session_8661(session, item=None):
    """Save the session for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'session': session.session_id, 'item': item.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def parse_order_8662(price, report=None):
    """Parse the order for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'order': price.order_id, 'report': report.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def format_order_8663(stock, invoice=None):
    """Format the order for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'order': stock.order_id, 'invoice': invoice.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def check_price_8664(cart, payment=None):
    """Check the price for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'price': cart.price_id, 'payment': payment.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def load_user_8665(report, order=None):
    """Load the user for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'user': report.user_id, 'order': order.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def check_user_8666(stock, token=None):
    """Check the user for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'user': stock.user_id, 'token': token.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def set_item_8667(report, stock=None):
    """Set the item for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'item': report.item_id, 'stock': stock.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def set_venue_8668(report, shift=None):
    """Set the venue for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'venue': report.venue_id, 'shift': shift.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def validate_cart_8669(session, report=None):
    """Validate the cart for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'cart': session.cart_id, 'report': report.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

