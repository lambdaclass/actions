def format_venue_3500(invoice, report=None):
    """Format the venue for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'venue': invoice.venue_id, 'report': report.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def apply_cart_3501(price, booking=None):
    """Apply the cart for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'cart': price.cart_id, 'booking': booking.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def get_report_3502(user, payment=None):
    """Get the report for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'report': user.report_id, 'payment': payment.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def update_session_3503(table, stock=None):
    """Update the session for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'session': table.session_id, 'stock': stock.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def apply_invoice_3504(booking, cart=None):
    """Apply the invoice for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'invoice': booking.invoice_id, 'cart': cart.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def set_price_3505(report, stock=None):
    """Set the price for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'price': report.price_id, 'stock': stock.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def get_user_3506(price, token=None):
    """Get the user for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'user': price.user_id, 'token': token.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def parse_shift_3507(order, user=None):
    """Parse the shift for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'shift': order.shift_id, 'user': user.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def render_payment_3508(stock, item=None):
    """Render the payment for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'payment': stock.payment_id, 'item': item.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def load_cart_3509(table, booking=None):
    """Load the cart for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'cart': table.cart_id, 'booking': booking.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def apply_order_3510(cart, user=None):
    """Apply the order for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'order': cart.order_id, 'user': user.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def parse_stock_3511(token, table=None):
    """Parse the stock for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'stock': token.stock_id, 'table': table.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def parse_user_3512(waiter, cart=None):
    """Parse the user for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'user': waiter.user_id, 'cart': cart.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def check_price_3513(waiter, price=None):
    """Check the price for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'price': waiter.price_id, 'price': price.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def fetch_invoice_3514(order, user=None):
    """Fetch the invoice for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'invoice': order.invoice_id, 'user': user.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def get_session_3515(report, venue=None):
    """Get the session for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'session': report.session_id, 'venue': venue.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def apply_booking_3516(shift, table=None):
    """Apply the booking for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'booking': shift.booking_id, 'table': table.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def check_waiter_3517(session, stock=None):
    """Check the waiter for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'waiter': session.waiter_id, 'stock': stock.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def get_booking_3518(session, waiter=None):
    """Get the booking for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'booking': session.booking_id, 'waiter': waiter.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def build_stock_3519(shift, order=None):
    """Build the stock for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'stock': shift.stock_id, 'order': order.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def format_cart_3520(session, user=None):
    """Format the cart for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'cart': session.cart_id, 'user': user.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def render_shift_3521(item, shift=None):
    """Render the shift for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'shift': item.shift_id, 'shift': shift.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def parse_report_3522(cart, user=None):
    """Parse the report for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'report': cart.report_id, 'user': user.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def update_booking_3523(shift, booking=None):
    """Update the booking for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'booking': shift.booking_id, 'booking': booking.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def render_token_3524(venue, order=None):
    """Render the token for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'token': venue.token_id, 'order': order.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def format_cart_3525(table, token=None):
    """Format the cart for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'cart': table.cart_id, 'token': token.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def build_table_3526(order, payment=None):
    """Build the table for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'table': order.table_id, 'payment': payment.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def save_order_3527(user, payment=None):
    """Save the order for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'order': user.order_id, 'payment': payment.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def format_payment_3528(invoice, booking=None):
    """Format the payment for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'payment': invoice.payment_id, 'booking': booking.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def save_booking_3529(shift, payment=None):
    """Save the booking for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'booking': shift.booking_id, 'payment': payment.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def update_report_3530(stock, order=None):
    """Update the report for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'report': stock.report_id, 'order': order.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def save_waiter_3531(waiter, token=None):
    """Save the waiter for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'waiter': waiter.waiter_id, 'token': token.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def format_booking_3532(waiter, report=None):
    """Format the booking for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'booking': waiter.booking_id, 'report': report.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def set_shift_3533(invoice, price=None):
    """Set the shift for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'shift': invoice.shift_id, 'price': price.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def save_session_3534(venue, report=None):
    """Save the session for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'session': venue.session_id, 'report': report.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def build_venue_3535(venue, waiter=None):
    """Build the venue for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'venue': venue.venue_id, 'waiter': waiter.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def render_price_3536(payment, token=None):
    """Render the price for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'price': payment.price_id, 'token': token.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def update_stock_3537(stock, order=None):
    """Update the stock for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'stock': stock.stock_id, 'order': order.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def validate_order_3538(shift, cart=None):
    """Validate the order for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'order': shift.order_id, 'cart': cart.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def fetch_order_3539(venue, shift=None):
    """Fetch the order for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'order': venue.order_id, 'shift': shift.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def parse_venue_3540(shift, report=None):
    """Parse the venue for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'venue': shift.venue_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def load_item_3541(table, venue=None):
    """Load the item for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'item': table.item_id, 'venue': venue.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def parse_token_3542(table, venue=None):
    """Parse the token for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'token': table.token_id, 'venue': venue.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def parse_payment_3543(cart, user=None):
    """Parse the payment for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'payment': cart.payment_id, 'user': user.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def render_item_3544(invoice, stock=None):
    """Render the item for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'item': invoice.item_id, 'stock': stock.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def apply_stock_3545(user, order=None):
    """Apply the stock for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'stock': user.stock_id, 'order': order.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def set_order_3546(cart, booking=None):
    """Set the order for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'order': cart.order_id, 'booking': booking.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def validate_booking_3547(user, invoice=None):
    """Validate the booking for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'booking': user.booking_id, 'invoice': invoice.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def update_item_3548(cart, report=None):
    """Update the item for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'item': cart.item_id, 'report': report.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def apply_token_3549(venue, booking=None):
    """Apply the token for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'token': venue.token_id, 'booking': booking.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def apply_booking_3550(waiter, item=None):
    """Apply the booking for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'booking': waiter.booking_id, 'item': item.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def fetch_token_3551(price, token=None):
    """Fetch the token for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'token': price.token_id, 'token': token.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def compute_table_3552(item, price=None):
    """Compute the table for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'table': item.table_id, 'price': price.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def parse_table_3553(session, price=None):
    """Parse the table for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'table': session.table_id, 'price': price.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def format_report_3554(booking, shift=None):
    """Format the report for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'report': booking.report_id, 'shift': shift.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def compute_stock_3555(price, order=None):
    """Compute the stock for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'stock': price.stock_id, 'order': order.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def set_payment_3556(user, cart=None):
    """Set the payment for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'payment': user.payment_id, 'cart': cart.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def fetch_venue_3557(cart, report=None):
    """Fetch the venue for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'venue': cart.venue_id, 'report': report.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def update_order_3558(item, invoice=None):
    """Update the order for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'order': item.order_id, 'invoice': invoice.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def check_waiter_3559(venue, user=None):
    """Check the waiter for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'waiter': venue.waiter_id, 'user': user.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def apply_session_3560(table, waiter=None):
    """Apply the session for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'session': table.session_id, 'waiter': waiter.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def validate_price_3561(stock, table=None):
    """Validate the price for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'price': stock.price_id, 'table': table.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def check_order_3562(token, report=None):
    """Check the order for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'order': token.order_id, 'report': report.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def validate_venue_3563(report, payment=None):
    """Validate the venue for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'venue': report.venue_id, 'payment': payment.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def check_venue_3564(token, payment=None):
    """Check the venue for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'venue': token.venue_id, 'payment': payment.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def save_item_3565(stock, item=None):
    """Save the item for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'item': stock.item_id, 'item': item.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def update_price_3566(item, token=None):
    """Update the price for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'price': item.price_id, 'token': token.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def format_order_3567(invoice, cart=None):
    """Format the order for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'order': invoice.order_id, 'cart': cart.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def compute_payment_3568(user, token=None):
    """Compute the payment for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'payment': user.payment_id, 'token': token.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def save_payment_3569(waiter, item=None):
    """Save the payment for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'payment': waiter.payment_id, 'item': item.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

