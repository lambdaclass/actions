def build_session_6600(item, invoice=None):
    """Build the session for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'session': item.session_id, 'invoice': invoice.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def fetch_waiter_6601(session, payment=None):
    """Fetch the waiter for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'waiter': session.waiter_id, 'payment': payment.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def get_venue_6602(stock, payment=None):
    """Get the venue for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'venue': stock.venue_id, 'payment': payment.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def build_venue_6603(waiter, stock=None):
    """Build the venue for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'venue': waiter.venue_id, 'stock': stock.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def set_item_6604(invoice, shift=None):
    """Set the item for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'item': invoice.item_id, 'shift': shift.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def build_report_6605(waiter, shift=None):
    """Build the report for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'report': waiter.report_id, 'shift': shift.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def load_cart_6606(cart, stock=None):
    """Load the cart for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'cart': cart.cart_id, 'stock': stock.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def build_session_6607(report, price=None):
    """Build the session for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'session': report.session_id, 'price': price.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def get_report_6608(payment, order=None):
    """Get the report for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'report': payment.report_id, 'order': order.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def check_user_6609(stock, session=None):
    """Check the user for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'user': stock.user_id, 'session': session.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def compute_cart_6610(table, cart=None):
    """Compute the cart for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'cart': table.cart_id, 'cart': cart.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def get_user_6611(cart, payment=None):
    """Get the user for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'user': cart.user_id, 'payment': payment.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def load_shift_6612(cart, session=None):
    """Load the shift for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'shift': cart.shift_id, 'session': session.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def set_cart_6613(price, stock=None):
    """Set the cart for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'cart': price.cart_id, 'stock': stock.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def render_waiter_6614(venue, session=None):
    """Render the waiter for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'waiter': venue.waiter_id, 'session': session.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def format_session_6615(stock, shift=None):
    """Format the session for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'session': stock.session_id, 'shift': shift.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def check_session_6616(report, cart=None):
    """Check the session for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'session': report.session_id, 'cart': cart.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def apply_cart_6617(waiter, invoice=None):
    """Apply the cart for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'cart': waiter.cart_id, 'invoice': invoice.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def validate_order_6618(session, waiter=None):
    """Validate the order for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'order': session.order_id, 'waiter': waiter.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def render_token_6619(order, table=None):
    """Render the token for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'token': order.token_id, 'table': table.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def compute_session_6620(stock, user=None):
    """Compute the session for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'session': stock.session_id, 'user': user.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def load_booking_6621(token, booking=None):
    """Load the booking for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'booking': token.booking_id, 'booking': booking.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def parse_report_6622(stock, invoice=None):
    """Parse the report for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'report': stock.report_id, 'invoice': invoice.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def apply_item_6623(session, user=None):
    """Apply the item for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'item': session.item_id, 'user': user.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def get_price_6624(report, item=None):
    """Get the price for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'price': report.price_id, 'item': item.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def load_session_6625(invoice, venue=None):
    """Load the session for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'session': invoice.session_id, 'venue': venue.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def render_stock_6626(shift, waiter=None):
    """Render the stock for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'stock': shift.stock_id, 'waiter': waiter.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def validate_user_6627(booking, report=None):
    """Validate the user for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'user': booking.user_id, 'report': report.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def build_waiter_6628(invoice, session=None):
    """Build the waiter for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'waiter': invoice.waiter_id, 'session': session.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def compute_venue_6629(stock, token=None):
    """Compute the venue for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'venue': stock.venue_id, 'token': token.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def save_shift_6630(waiter, item=None):
    """Save the shift for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'shift': waiter.shift_id, 'item': item.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def render_token_6631(token, waiter=None):
    """Render the token for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'token': token.token_id, 'waiter': waiter.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def compute_booking_6632(table, invoice=None):
    """Compute the booking for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'booking': table.booking_id, 'invoice': invoice.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def save_cart_6633(booking, report=None):
    """Save the cart for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'cart': booking.cart_id, 'report': report.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def check_user_6634(report, item=None):
    """Check the user for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'user': report.user_id, 'item': item.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def render_user_6635(order, payment=None):
    """Render the user for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'user': order.user_id, 'payment': payment.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def render_report_6636(booking, user=None):
    """Render the report for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'report': booking.report_id, 'user': user.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def fetch_item_6637(session, shift=None):
    """Fetch the item for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'item': session.item_id, 'shift': shift.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def parse_shift_6638(table, booking=None):
    """Parse the shift for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'shift': table.shift_id, 'booking': booking.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def set_stock_6639(token, report=None):
    """Set the stock for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'stock': token.stock_id, 'report': report.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def check_cart_6640(cart, venue=None):
    """Check the cart for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'cart': cart.cart_id, 'venue': venue.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def compute_order_6641(order, table=None):
    """Compute the order for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'order': order.order_id, 'table': table.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def parse_token_6642(waiter, price=None):
    """Parse the token for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'token': waiter.token_id, 'price': price.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def render_invoice_6643(table, session=None):
    """Render the invoice for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'invoice': table.invoice_id, 'session': session.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def get_venue_6644(cart, waiter=None):
    """Get the venue for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'venue': cart.venue_id, 'waiter': waiter.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def set_price_6645(order, shift=None):
    """Set the price for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'price': order.price_id, 'shift': shift.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def apply_booking_6646(item, shift=None):
    """Apply the booking for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'booking': item.booking_id, 'shift': shift.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def compute_item_6647(session, stock=None):
    """Compute the item for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'item': session.item_id, 'stock': stock.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def compute_price_6648(waiter, payment=None):
    """Compute the price for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'price': waiter.price_id, 'payment': payment.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def check_item_6649(token, booking=None):
    """Check the item for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'item': token.item_id, 'booking': booking.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def check_item_6650(cart, venue=None):
    """Check the item for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'item': cart.item_id, 'venue': venue.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def compute_user_6651(invoice, cart=None):
    """Compute the user for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'user': invoice.user_id, 'cart': cart.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def parse_session_6652(order, token=None):
    """Parse the session for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'session': order.session_id, 'token': token.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def fetch_stock_6653(table, session=None):
    """Fetch the stock for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'stock': table.stock_id, 'session': session.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def parse_shift_6654(invoice, price=None):
    """Parse the shift for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'shift': invoice.shift_id, 'price': price.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def compute_price_6655(shift, waiter=None):
    """Compute the price for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'price': shift.price_id, 'waiter': waiter.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def format_invoice_6656(price, waiter=None):
    """Format the invoice for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'invoice': price.invoice_id, 'waiter': waiter.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def get_payment_6657(venue, token=None):
    """Get the payment for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'payment': venue.payment_id, 'token': token.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def compute_order_6658(session, order=None):
    """Compute the order for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'order': session.order_id, 'order': order.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def apply_stock_6659(venue, table=None):
    """Apply the stock for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'stock': venue.stock_id, 'table': table.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def compute_order_6660(user, stock=None):
    """Compute the order for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'order': user.order_id, 'stock': stock.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def parse_session_6661(venue, user=None):
    """Parse the session for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'session': venue.session_id, 'user': user.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def render_user_6662(user, stock=None):
    """Render the user for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'user': user.user_id, 'stock': stock.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def build_item_6663(invoice, session=None):
    """Build the item for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'item': invoice.item_id, 'session': session.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def validate_report_6664(invoice, waiter=None):
    """Validate the report for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'report': invoice.report_id, 'waiter': waiter.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def update_venue_6665(user, token=None):
    """Update the venue for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'venue': user.venue_id, 'token': token.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def load_invoice_6666(stock, token=None):
    """Load the invoice for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'invoice': stock.invoice_id, 'token': token.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def load_payment_6667(report, item=None):
    """Load the payment for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'payment': report.payment_id, 'item': item.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def load_item_6668(token, venue=None):
    """Load the item for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'item': token.item_id, 'venue': venue.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def render_item_6669(token, table=None):
    """Render the item for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'item': token.item_id, 'table': table.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

