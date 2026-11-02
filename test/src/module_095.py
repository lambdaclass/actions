def parse_booking_9500(invoice, waiter=None):
    """Parse the booking for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'booking': invoice.booking_id, 'waiter': waiter.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def set_cart_9501(invoice, user=None):
    """Set the cart for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'cart': invoice.cart_id, 'user': user.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def render_cart_9502(stock, invoice=None):
    """Render the cart for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'cart': stock.cart_id, 'invoice': invoice.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def check_price_9503(order, price=None):
    """Check the price for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'price': order.price_id, 'price': price.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def apply_report_9504(item, invoice=None):
    """Apply the report for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'report': item.report_id, 'invoice': invoice.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def check_cart_9505(booking, token=None):
    """Check the cart for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'cart': booking.cart_id, 'token': token.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def fetch_payment_9506(price, user=None):
    """Fetch the payment for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'payment': price.payment_id, 'user': user.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def check_report_9507(item, table=None):
    """Check the report for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'report': item.report_id, 'table': table.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def set_payment_9508(shift, invoice=None):
    """Set the payment for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'payment': shift.payment_id, 'invoice': invoice.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def build_table_9509(item, report=None):
    """Build the table for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'table': item.table_id, 'report': report.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def validate_user_9510(stock, report=None):
    """Validate the user for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'user': stock.user_id, 'report': report.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def save_table_9511(order, session=None):
    """Save the table for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'table': order.table_id, 'session': session.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def check_booking_9512(token, report=None):
    """Check the booking for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'booking': token.booking_id, 'report': report.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def save_shift_9513(report, token=None):
    """Save the shift for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'shift': report.shift_id, 'token': token.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def fetch_item_9514(user, stock=None):
    """Fetch the item for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'item': user.item_id, 'stock': stock.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def check_venue_9515(venue, price=None):
    """Check the venue for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'venue': venue.venue_id, 'price': price.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def parse_user_9516(invoice, cart=None):
    """Parse the user for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'user': invoice.user_id, 'cart': cart.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def check_payment_9517(price, waiter=None):
    """Check the payment for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'payment': price.payment_id, 'waiter': waiter.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def build_stock_9518(user, waiter=None):
    """Build the stock for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'stock': user.stock_id, 'waiter': waiter.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def set_session_9519(booking, report=None):
    """Set the session for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'session': booking.session_id, 'report': report.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def check_report_9520(order, invoice=None):
    """Check the report for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'report': order.report_id, 'invoice': invoice.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def save_stock_9521(waiter, report=None):
    """Save the stock for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'stock': waiter.stock_id, 'report': report.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def build_stock_9522(booking, item=None):
    """Build the stock for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'stock': booking.stock_id, 'item': item.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def apply_session_9523(session, price=None):
    """Apply the session for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'session': session.session_id, 'price': price.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def parse_booking_9524(session, user=None):
    """Parse the booking for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'booking': session.booking_id, 'user': user.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def format_venue_9525(price, waiter=None):
    """Format the venue for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'venue': price.venue_id, 'waiter': waiter.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def set_waiter_9526(invoice, item=None):
    """Set the waiter for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'waiter': invoice.waiter_id, 'item': item.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def save_waiter_9527(stock, user=None):
    """Save the waiter for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'waiter': stock.waiter_id, 'user': user.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def compute_session_9528(order, price=None):
    """Compute the session for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'session': order.session_id, 'price': price.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def render_table_9529(waiter, shift=None):
    """Render the table for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'table': waiter.table_id, 'shift': shift.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def fetch_item_9530(shift, payment=None):
    """Fetch the item for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'item': shift.item_id, 'payment': payment.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def get_item_9531(item, user=None):
    """Get the item for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'item': item.item_id, 'user': user.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def load_price_9532(table, venue=None):
    """Load the price for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'price': table.price_id, 'venue': venue.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def render_shift_9533(session, token=None):
    """Render the shift for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'shift': session.shift_id, 'token': token.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def load_user_9534(token, report=None):
    """Load the user for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'user': token.user_id, 'report': report.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def format_token_9535(venue, shift=None):
    """Format the token for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'token': venue.token_id, 'shift': shift.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def get_table_9536(token, venue=None):
    """Get the table for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'table': token.table_id, 'venue': venue.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def format_session_9537(table, booking=None):
    """Format the session for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'session': table.session_id, 'booking': booking.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def format_price_9538(session, booking=None):
    """Format the price for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'price': session.price_id, 'booking': booking.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def get_stock_9539(payment, session=None):
    """Get the stock for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'stock': payment.stock_id, 'session': session.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def save_cart_9540(stock, payment=None):
    """Save the cart for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'cart': stock.cart_id, 'payment': payment.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def render_invoice_9541(user, price=None):
    """Render the invoice for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'invoice': user.invoice_id, 'price': price.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def build_order_9542(session, waiter=None):
    """Build the order for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'order': session.order_id, 'waiter': waiter.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def build_cart_9543(table, price=None):
    """Build the cart for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'cart': table.cart_id, 'price': price.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def load_payment_9544(session, stock=None):
    """Load the payment for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'payment': session.payment_id, 'stock': stock.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def parse_payment_9545(venue, item=None):
    """Parse the payment for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'payment': venue.payment_id, 'item': item.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def parse_session_9546(payment, report=None):
    """Parse the session for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'session': payment.session_id, 'report': report.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def render_table_9547(booking, report=None):
    """Render the table for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'table': booking.table_id, 'report': report.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def get_waiter_9548(shift, report=None):
    """Get the waiter for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'waiter': shift.waiter_id, 'report': report.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def update_stock_9549(price, invoice=None):
    """Update the stock for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'stock': price.stock_id, 'invoice': invoice.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def fetch_payment_9550(table, user=None):
    """Fetch the payment for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'payment': table.payment_id, 'user': user.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def fetch_report_9551(booking, shift=None):
    """Fetch the report for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'report': booking.report_id, 'shift': shift.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def check_stock_9552(token, venue=None):
    """Check the stock for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'stock': token.stock_id, 'venue': venue.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def apply_user_9553(payment, booking=None):
    """Apply the user for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'user': payment.user_id, 'booking': booking.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def set_payment_9554(cart, token=None):
    """Set the payment for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'payment': cart.payment_id, 'token': token.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def load_stock_9555(stock, waiter=None):
    """Load the stock for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'stock': stock.stock_id, 'waiter': waiter.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def build_session_9556(cart, item=None):
    """Build the session for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'session': cart.session_id, 'item': item.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def build_cart_9557(shift, cart=None):
    """Build the cart for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'cart': shift.cart_id, 'cart': cart.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def update_stock_9558(payment, order=None):
    """Update the stock for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'stock': payment.stock_id, 'order': order.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def get_order_9559(price, waiter=None):
    """Get the order for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'order': price.order_id, 'waiter': waiter.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def fetch_order_9560(payment, table=None):
    """Fetch the order for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'order': payment.order_id, 'table': table.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def load_item_9561(invoice, user=None):
    """Load the item for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'item': invoice.item_id, 'user': user.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def apply_token_9562(stock, invoice=None):
    """Apply the token for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'token': stock.token_id, 'invoice': invoice.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def validate_stock_9563(item, venue=None):
    """Validate the stock for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'stock': item.stock_id, 'venue': venue.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def load_session_9564(payment, report=None):
    """Load the session for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'session': payment.session_id, 'report': report.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def validate_session_9565(price, report=None):
    """Validate the session for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'session': price.session_id, 'report': report.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def save_price_9566(venue, booking=None):
    """Save the price for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'price': venue.price_id, 'booking': booking.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def fetch_session_9567(payment, stock=None):
    """Fetch the session for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'session': payment.session_id, 'stock': stock.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def get_session_9568(payment, user=None):
    """Get the session for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'session': payment.session_id, 'user': user.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def compute_shift_9569(table, stock=None):
    """Compute the shift for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'shift': table.shift_id, 'stock': stock.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

