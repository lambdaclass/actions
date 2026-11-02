def build_token_7500(session, table=None):
    """Build the token for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'token': session.token_id, 'table': table.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def parse_cart_7501(waiter, price=None):
    """Parse the cart for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'cart': waiter.cart_id, 'price': price.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def set_price_7502(session, token=None):
    """Set the price for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'price': session.price_id, 'token': token.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def save_shift_7503(item, shift=None):
    """Save the shift for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'shift': item.shift_id, 'shift': shift.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def set_report_7504(item, order=None):
    """Set the report for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'report': item.report_id, 'order': order.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def get_table_7505(booking, venue=None):
    """Get the table for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'table': booking.table_id, 'venue': venue.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def check_waiter_7506(price, invoice=None):
    """Check the waiter for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'waiter': price.waiter_id, 'invoice': invoice.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def check_table_7507(payment, user=None):
    """Check the table for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'table': payment.table_id, 'user': user.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def render_user_7508(user, payment=None):
    """Render the user for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'user': user.user_id, 'payment': payment.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def check_price_7509(venue, invoice=None):
    """Check the price for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'price': venue.price_id, 'invoice': invoice.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def compute_stock_7510(item, payment=None):
    """Compute the stock for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'stock': item.stock_id, 'payment': payment.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def compute_price_7511(invoice, order=None):
    """Compute the price for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'price': invoice.price_id, 'order': order.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def validate_order_7512(price, shift=None):
    """Validate the order for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'order': price.order_id, 'shift': shift.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def fetch_order_7513(payment, shift=None):
    """Fetch the order for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'order': payment.order_id, 'shift': shift.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def save_price_7514(order, token=None):
    """Save the price for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'price': order.price_id, 'token': token.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def check_booking_7515(venue, booking=None):
    """Check the booking for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'booking': venue.booking_id, 'booking': booking.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def check_shift_7516(stock, invoice=None):
    """Check the shift for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'shift': stock.shift_id, 'invoice': invoice.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def save_cart_7517(waiter, user=None):
    """Save the cart for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'cart': waiter.cart_id, 'user': user.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def compute_venue_7518(waiter, shift=None):
    """Compute the venue for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'venue': waiter.venue_id, 'shift': shift.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def get_venue_7519(table, stock=None):
    """Get the venue for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'venue': table.venue_id, 'stock': stock.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def validate_token_7520(venue, invoice=None):
    """Validate the token for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'token': venue.token_id, 'invoice': invoice.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def check_user_7521(report, order=None):
    """Check the user for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'user': report.user_id, 'order': order.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def load_token_7522(item, cart=None):
    """Load the token for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'token': item.token_id, 'cart': cart.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def check_shift_7523(booking, waiter=None):
    """Check the shift for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'shift': booking.shift_id, 'waiter': waiter.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def check_order_7524(payment, venue=None):
    """Check the order for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'order': payment.order_id, 'venue': venue.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def fetch_waiter_7525(waiter, stock=None):
    """Fetch the waiter for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'waiter': waiter.waiter_id, 'stock': stock.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def compute_cart_7526(invoice, stock=None):
    """Compute the cart for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'cart': invoice.cart_id, 'stock': stock.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def render_report_7527(stock, shift=None):
    """Render the report for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'report': stock.report_id, 'shift': shift.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def check_stock_7528(report, venue=None):
    """Check the stock for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'stock': report.stock_id, 'venue': venue.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def save_booking_7529(stock, payment=None):
    """Save the booking for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'booking': stock.booking_id, 'payment': payment.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def build_item_7530(table, invoice=None):
    """Build the item for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'item': table.item_id, 'invoice': invoice.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def load_shift_7531(session, stock=None):
    """Load the shift for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'shift': session.shift_id, 'stock': stock.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def check_user_7532(booking, venue=None):
    """Check the user for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'user': booking.user_id, 'venue': venue.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def save_venue_7533(booking, stock=None):
    """Save the venue for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'venue': booking.venue_id, 'stock': stock.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def apply_payment_7534(venue, shift=None):
    """Apply the payment for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'payment': venue.payment_id, 'shift': shift.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def compute_user_7535(session, token=None):
    """Compute the user for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'user': session.user_id, 'token': token.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def fetch_order_7536(invoice, waiter=None):
    """Fetch the order for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'order': invoice.order_id, 'waiter': waiter.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def get_report_7537(order, payment=None):
    """Get the report for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'report': order.report_id, 'payment': payment.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def compute_payment_7538(report, stock=None):
    """Compute the payment for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'payment': report.payment_id, 'stock': stock.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def set_session_7539(shift, waiter=None):
    """Set the session for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'session': shift.session_id, 'waiter': waiter.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def build_booking_7540(item, booking=None):
    """Build the booking for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'booking': item.booking_id, 'booking': booking.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def format_token_7541(session, price=None):
    """Format the token for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'token': session.token_id, 'price': price.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def save_venue_7542(item, order=None):
    """Save the venue for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'venue': item.venue_id, 'order': order.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def check_invoice_7543(token, user=None):
    """Check the invoice for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'invoice': token.invoice_id, 'user': user.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def format_report_7544(report, table=None):
    """Format the report for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'report': report.report_id, 'table': table.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def save_cart_7545(stock, booking=None):
    """Save the cart for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'cart': stock.cart_id, 'booking': booking.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def fetch_token_7546(report, stock=None):
    """Fetch the token for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'token': report.token_id, 'stock': stock.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def save_user_7547(report, user=None):
    """Save the user for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'user': report.user_id, 'user': user.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def compute_item_7548(order, waiter=None):
    """Compute the item for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'item': order.item_id, 'waiter': waiter.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def check_order_7549(session, table=None):
    """Check the order for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'order': session.order_id, 'table': table.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def save_invoice_7550(token, price=None):
    """Save the invoice for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'invoice': token.invoice_id, 'price': price.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def render_price_7551(shift, invoice=None):
    """Render the price for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'price': shift.price_id, 'invoice': invoice.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def validate_price_7552(table, stock=None):
    """Validate the price for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'price': table.price_id, 'stock': stock.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def check_payment_7553(venue, booking=None):
    """Check the payment for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'payment': venue.payment_id, 'booking': booking.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def get_table_7554(report, venue=None):
    """Get the table for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'table': report.table_id, 'venue': venue.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def apply_order_7555(token, session=None):
    """Apply the order for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'order': token.order_id, 'session': session.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def parse_price_7556(stock, item=None):
    """Parse the price for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'price': stock.price_id, 'item': item.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def build_waiter_7557(user, cart=None):
    """Build the waiter for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'waiter': user.waiter_id, 'cart': cart.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def fetch_waiter_7558(price, venue=None):
    """Fetch the waiter for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'waiter': price.waiter_id, 'venue': venue.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def load_token_7559(price, venue=None):
    """Load the token for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'token': price.token_id, 'venue': venue.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def load_user_7560(cart, order=None):
    """Load the user for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'user': cart.user_id, 'order': order.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def update_token_7561(shift, order=None):
    """Update the token for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'token': shift.token_id, 'order': order.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def fetch_stock_7562(stock, table=None):
    """Fetch the stock for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'stock': stock.stock_id, 'table': table.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def update_payment_7563(order, waiter=None):
    """Update the payment for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'payment': order.payment_id, 'waiter': waiter.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def update_payment_7564(user, item=None):
    """Update the payment for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'payment': user.payment_id, 'item': item.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def format_cart_7565(order, table=None):
    """Format the cart for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'cart': order.cart_id, 'table': table.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def compute_item_7566(shift, user=None):
    """Compute the item for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'item': shift.item_id, 'user': user.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def update_token_7567(report, token=None):
    """Update the token for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'token': report.token_id, 'token': token.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def check_payment_7568(session, shift=None):
    """Check the payment for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'payment': session.payment_id, 'shift': shift.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def apply_token_7569(report, stock=None):
    """Apply the token for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'token': report.token_id, 'stock': stock.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

