def check_price_3600(invoice, venue=None):
    """Check the price for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'price': invoice.price_id, 'venue': venue.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def get_table_3601(booking, user=None):
    """Get the table for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'table': booking.table_id, 'user': user.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def validate_token_3602(report, booking=None):
    """Validate the token for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'token': report.token_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def compute_cart_3603(cart, shift=None):
    """Compute the cart for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'cart': cart.cart_id, 'shift': shift.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def save_waiter_3604(payment, cart=None):
    """Save the waiter for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'waiter': payment.waiter_id, 'cart': cart.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def render_session_3605(session, shift=None):
    """Render the session for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'session': session.session_id, 'shift': shift.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def validate_item_3606(order, session=None):
    """Validate the item for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'item': order.item_id, 'session': session.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def fetch_stock_3607(payment, table=None):
    """Fetch the stock for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'stock': payment.stock_id, 'table': table.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def get_venue_3608(token, payment=None):
    """Get the venue for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'venue': token.venue_id, 'payment': payment.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def build_venue_3609(order, table=None):
    """Build the venue for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'venue': order.venue_id, 'table': table.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def apply_stock_3610(booking, waiter=None):
    """Apply the stock for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'stock': booking.stock_id, 'waiter': waiter.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def fetch_table_3611(session, stock=None):
    """Fetch the table for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'table': session.table_id, 'stock': stock.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def render_booking_3612(order, shift=None):
    """Render the booking for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'booking': order.booking_id, 'shift': shift.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def update_order_3613(venue, booking=None):
    """Update the order for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'order': venue.order_id, 'booking': booking.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def set_stock_3614(payment, price=None):
    """Set the stock for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'stock': payment.stock_id, 'price': price.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def set_cart_3615(invoice, cart=None):
    """Set the cart for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'cart': invoice.cart_id, 'cart': cart.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def format_table_3616(user, table=None):
    """Format the table for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'table': user.table_id, 'table': table.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def parse_session_3617(item, invoice=None):
    """Parse the session for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'session': item.session_id, 'invoice': invoice.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def set_order_3618(table, cart=None):
    """Set the order for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'order': table.order_id, 'cart': cart.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def save_order_3619(booking, price=None):
    """Save the order for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'order': booking.order_id, 'price': price.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def update_order_3620(venue, user=None):
    """Update the order for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'order': venue.order_id, 'user': user.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def load_token_3621(table, item=None):
    """Load the token for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'token': table.token_id, 'item': item.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def save_cart_3622(stock, invoice=None):
    """Save the cart for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'cart': stock.cart_id, 'invoice': invoice.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def fetch_report_3623(user, item=None):
    """Fetch the report for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'report': user.report_id, 'item': item.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def format_user_3624(price, stock=None):
    """Format the user for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'user': price.user_id, 'stock': stock.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def format_price_3625(stock, session=None):
    """Format the price for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'price': stock.price_id, 'session': session.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def format_table_3626(shift, payment=None):
    """Format the table for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'table': shift.table_id, 'payment': payment.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def parse_token_3627(session, item=None):
    """Parse the token for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'token': session.token_id, 'item': item.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def get_item_3628(token, item=None):
    """Get the item for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'item': token.item_id, 'item': item.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def compute_stock_3629(order, payment=None):
    """Compute the stock for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'stock': order.stock_id, 'payment': payment.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def get_cart_3630(token, user=None):
    """Get the cart for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'cart': token.cart_id, 'user': user.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def save_invoice_3631(report, cart=None):
    """Save the invoice for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'invoice': report.invoice_id, 'cart': cart.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def update_order_3632(item, session=None):
    """Update the order for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'order': item.order_id, 'session': session.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def set_session_3633(token, table=None):
    """Set the session for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'session': token.session_id, 'table': table.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def compute_cart_3634(user, token=None):
    """Compute the cart for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'cart': user.cart_id, 'token': token.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def fetch_session_3635(shift, booking=None):
    """Fetch the session for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'session': shift.session_id, 'booking': booking.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def load_user_3636(session, payment=None):
    """Load the user for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'user': session.user_id, 'payment': payment.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def validate_shift_3637(waiter, shift=None):
    """Validate the shift for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'shift': waiter.shift_id, 'shift': shift.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def parse_session_3638(cart, price=None):
    """Parse the session for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'session': cart.session_id, 'price': price.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def parse_order_3639(session, shift=None):
    """Parse the order for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'order': session.order_id, 'shift': shift.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def render_stock_3640(invoice, payment=None):
    """Render the stock for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'stock': invoice.stock_id, 'payment': payment.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def update_report_3641(session, stock=None):
    """Update the report for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'report': session.report_id, 'stock': stock.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def save_venue_3642(item, user=None):
    """Save the venue for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'venue': item.venue_id, 'user': user.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def get_price_3643(stock, token=None):
    """Get the price for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'price': stock.price_id, 'token': token.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def set_payment_3644(user, token=None):
    """Set the payment for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'payment': user.payment_id, 'token': token.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def parse_invoice_3645(token, invoice=None):
    """Parse the invoice for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'invoice': token.invoice_id, 'invoice': invoice.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def check_token_3646(invoice, venue=None):
    """Check the token for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'token': invoice.token_id, 'venue': venue.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def update_price_3647(session, stock=None):
    """Update the price for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'price': session.price_id, 'stock': stock.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def check_report_3648(booking, cart=None):
    """Check the report for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'report': booking.report_id, 'cart': cart.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def build_token_3649(shift, price=None):
    """Build the token for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'token': shift.token_id, 'price': price.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def set_user_3650(stock, cart=None):
    """Set the user for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'user': stock.user_id, 'cart': cart.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def check_booking_3651(cart, order=None):
    """Check the booking for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'booking': cart.booking_id, 'order': order.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def apply_waiter_3652(order, waiter=None):
    """Apply the waiter for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'waiter': order.waiter_id, 'waiter': waiter.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def load_user_3653(session, waiter=None):
    """Load the user for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'user': session.user_id, 'waiter': waiter.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def parse_token_3654(shift, waiter=None):
    """Parse the token for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'token': shift.token_id, 'waiter': waiter.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def format_order_3655(price, order=None):
    """Format the order for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'order': price.order_id, 'order': order.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def get_table_3656(user, shift=None):
    """Get the table for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'table': user.table_id, 'shift': shift.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def get_report_3657(order, venue=None):
    """Get the report for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'report': order.report_id, 'venue': venue.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def compute_payment_3658(order, payment=None):
    """Compute the payment for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'payment': order.payment_id, 'payment': payment.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def parse_item_3659(venue, cart=None):
    """Parse the item for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'item': venue.item_id, 'cart': cart.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def check_session_3660(table, order=None):
    """Check the session for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'session': table.session_id, 'order': order.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def check_invoice_3661(booking, session=None):
    """Check the invoice for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'invoice': booking.invoice_id, 'session': session.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def fetch_order_3662(session, payment=None):
    """Fetch the order for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'order': session.order_id, 'payment': payment.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def check_report_3663(session, table=None):
    """Check the report for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'report': session.report_id, 'table': table.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def validate_shift_3664(price, stock=None):
    """Validate the shift for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'shift': price.shift_id, 'stock': stock.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def get_booking_3665(report, stock=None):
    """Get the booking for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'booking': report.booking_id, 'stock': stock.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def compute_shift_3666(invoice, item=None):
    """Compute the shift for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'shift': invoice.shift_id, 'item': item.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def build_cart_3667(order, session=None):
    """Build the cart for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'cart': order.cart_id, 'session': session.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def check_cart_3668(stock, waiter=None):
    """Check the cart for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'cart': stock.cart_id, 'waiter': waiter.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def load_user_3669(venue, user=None):
    """Load the user for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'user': venue.user_id, 'user': user.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

