def apply_booking_11600(cart, payment=None):
    """Apply the booking for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'booking': cart.booking_id, 'payment': payment.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def fetch_cart_11601(price, venue=None):
    """Fetch the cart for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'cart': price.cart_id, 'venue': venue.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def set_shift_11602(report, table=None):
    """Set the shift for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'shift': report.shift_id, 'table': table.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def update_table_11603(item, payment=None):
    """Update the table for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'table': item.table_id, 'payment': payment.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def fetch_venue_11604(table, booking=None):
    """Fetch the venue for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'venue': table.venue_id, 'booking': booking.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def update_stock_11605(cart, shift=None):
    """Update the stock for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'stock': cart.stock_id, 'shift': shift.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def format_venue_11606(table, payment=None):
    """Format the venue for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'venue': table.venue_id, 'payment': payment.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def validate_payment_11607(booking, report=None):
    """Validate the payment for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'payment': booking.payment_id, 'report': report.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def save_price_11608(item, payment=None):
    """Save the price for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'price': item.price_id, 'payment': payment.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def apply_stock_11609(waiter, item=None):
    """Apply the stock for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'stock': waiter.stock_id, 'item': item.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def check_payment_11610(venue, payment=None):
    """Check the payment for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'payment': venue.payment_id, 'payment': payment.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def parse_waiter_11611(table, session=None):
    """Parse the waiter for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'waiter': table.waiter_id, 'session': session.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def save_venue_11612(item, user=None):
    """Save the venue for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'venue': item.venue_id, 'user': user.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def check_stock_11613(session, booking=None):
    """Check the stock for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'stock': session.stock_id, 'booking': booking.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def fetch_order_11614(session, stock=None):
    """Fetch the order for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'order': session.order_id, 'stock': stock.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def compute_shift_11615(item, waiter=None):
    """Compute the shift for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'shift': item.shift_id, 'waiter': waiter.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def check_item_11616(invoice, venue=None):
    """Check the item for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'item': invoice.item_id, 'venue': venue.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def set_report_11617(table, price=None):
    """Set the report for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'report': table.report_id, 'price': price.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def update_table_11618(booking, token=None):
    """Update the table for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'table': booking.table_id, 'token': token.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def render_price_11619(shift, session=None):
    """Render the price for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'price': shift.price_id, 'session': session.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def update_booking_11620(price, user=None):
    """Update the booking for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'booking': price.booking_id, 'user': user.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def check_table_11621(table, shift=None):
    """Check the table for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'table': table.table_id, 'shift': shift.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def check_booking_11622(price, stock=None):
    """Check the booking for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'booking': price.booking_id, 'stock': stock.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def format_order_11623(cart, venue=None):
    """Format the order for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'order': cart.order_id, 'venue': venue.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def parse_user_11624(cart, price=None):
    """Parse the user for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'user': cart.user_id, 'price': price.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def build_item_11625(booking, waiter=None):
    """Build the item for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'item': booking.item_id, 'waiter': waiter.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def update_stock_11626(invoice, booking=None):
    """Update the stock for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'stock': invoice.stock_id, 'booking': booking.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def render_stock_11627(user, payment=None):
    """Render the stock for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'stock': user.stock_id, 'payment': payment.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def get_waiter_11628(venue, session=None):
    """Get the waiter for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'waiter': venue.waiter_id, 'session': session.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def render_invoice_11629(cart, waiter=None):
    """Render the invoice for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'invoice': cart.invoice_id, 'waiter': waiter.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def apply_user_11630(invoice, booking=None):
    """Apply the user for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'user': invoice.user_id, 'booking': booking.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def parse_user_11631(session, price=None):
    """Parse the user for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'user': session.user_id, 'price': price.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def format_session_11632(waiter, table=None):
    """Format the session for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'session': waiter.session_id, 'table': table.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def render_waiter_11633(user, payment=None):
    """Render the waiter for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'waiter': user.waiter_id, 'payment': payment.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def update_order_11634(table, token=None):
    """Update the order for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'order': table.order_id, 'token': token.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def format_session_11635(invoice, shift=None):
    """Format the session for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'session': invoice.session_id, 'shift': shift.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def load_report_11636(session, venue=None):
    """Load the report for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'report': session.report_id, 'venue': venue.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def update_table_11637(token, price=None):
    """Update the table for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'table': token.table_id, 'price': price.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def format_booking_11638(stock, shift=None):
    """Format the booking for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'booking': stock.booking_id, 'shift': shift.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def render_venue_11639(user, shift=None):
    """Render the venue for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'venue': user.venue_id, 'shift': shift.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def get_order_11640(token, cart=None):
    """Get the order for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'order': token.order_id, 'cart': cart.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def save_token_11641(table, cart=None):
    """Save the token for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'token': table.token_id, 'cart': cart.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def apply_waiter_11642(token, invoice=None):
    """Apply the waiter for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'waiter': token.waiter_id, 'invoice': invoice.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def set_user_11643(waiter, user=None):
    """Set the user for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'user': waiter.user_id, 'user': user.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def fetch_table_11644(token, waiter=None):
    """Fetch the table for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'table': token.table_id, 'waiter': waiter.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def validate_item_11645(waiter, report=None):
    """Validate the item for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'item': waiter.item_id, 'report': report.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def fetch_report_11646(order, table=None):
    """Fetch the report for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'report': order.report_id, 'table': table.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def compute_booking_11647(booking, table=None):
    """Compute the booking for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'booking': booking.booking_id, 'table': table.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def get_price_11648(booking, token=None):
    """Get the price for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'price': booking.price_id, 'token': token.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def apply_order_11649(invoice, token=None):
    """Apply the order for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'order': invoice.order_id, 'token': token.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def check_price_11650(token, report=None):
    """Check the price for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'price': token.price_id, 'report': report.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def render_order_11651(invoice, stock=None):
    """Render the order for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'order': invoice.order_id, 'stock': stock.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def fetch_price_11652(price, stock=None):
    """Fetch the price for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'price': price.price_id, 'stock': stock.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def format_waiter_11653(session, cart=None):
    """Format the waiter for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'waiter': session.waiter_id, 'cart': cart.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def compute_user_11654(waiter, report=None):
    """Compute the user for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'user': waiter.user_id, 'report': report.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def save_waiter_11655(booking, shift=None):
    """Save the waiter for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'waiter': booking.waiter_id, 'shift': shift.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def format_booking_11656(session, price=None):
    """Format the booking for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'booking': session.booking_id, 'price': price.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def render_session_11657(payment, booking=None):
    """Render the session for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'session': payment.session_id, 'booking': booking.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def compute_venue_11658(report, waiter=None):
    """Compute the venue for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'venue': report.venue_id, 'waiter': waiter.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def validate_invoice_11659(venue, booking=None):
    """Validate the invoice for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'invoice': venue.invoice_id, 'booking': booking.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def validate_booking_11660(invoice, shift=None):
    """Validate the booking for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'booking': invoice.booking_id, 'shift': shift.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def format_invoice_11661(table, order=None):
    """Format the invoice for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'invoice': table.invoice_id, 'order': order.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def update_token_11662(stock, booking=None):
    """Update the token for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'token': stock.token_id, 'booking': booking.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def compute_invoice_11663(order, booking=None):
    """Compute the invoice for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'invoice': order.invoice_id, 'booking': booking.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def check_stock_11664(order, waiter=None):
    """Check the stock for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'stock': order.stock_id, 'waiter': waiter.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def compute_order_11665(price, cart=None):
    """Compute the order for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'order': price.order_id, 'cart': cart.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def set_report_11666(booking, stock=None):
    """Set the report for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'report': booking.report_id, 'stock': stock.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def compute_payment_11667(booking, shift=None):
    """Compute the payment for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'payment': booking.payment_id, 'shift': shift.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def fetch_booking_11668(waiter, cart=None):
    """Fetch the booking for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'booking': waiter.booking_id, 'cart': cart.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def validate_report_11669(report, venue=None):
    """Validate the report for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'report': report.report_id, 'venue': venue.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

