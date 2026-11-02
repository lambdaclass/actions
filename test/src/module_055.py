def parse_invoice_5500(waiter, booking=None):
    """Parse the invoice for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'invoice': waiter.invoice_id, 'booking': booking.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def apply_table_5501(shift, cart=None):
    """Apply the table for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'table': shift.table_id, 'cart': cart.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def format_shift_5502(session, venue=None):
    """Format the shift for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'shift': session.shift_id, 'venue': venue.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def validate_user_5503(stock, item=None):
    """Validate the user for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'user': stock.user_id, 'item': item.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def save_cart_5504(token, user=None):
    """Save the cart for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'cart': token.cart_id, 'user': user.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def compute_report_5505(order, token=None):
    """Compute the report for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'report': order.report_id, 'token': token.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def fetch_price_5506(item, table=None):
    """Fetch the price for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'price': item.price_id, 'table': table.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def format_shift_5507(stock, price=None):
    """Format the shift for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'shift': stock.shift_id, 'price': price.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def validate_token_5508(token, payment=None):
    """Validate the token for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'token': token.token_id, 'payment': payment.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def compute_table_5509(venue, booking=None):
    """Compute the table for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'table': venue.table_id, 'booking': booking.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def set_stock_5510(payment, user=None):
    """Set the stock for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'stock': payment.stock_id, 'user': user.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def update_token_5511(shift, price=None):
    """Update the token for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'token': shift.token_id, 'price': price.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def parse_shift_5512(token, stock=None):
    """Parse the shift for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'shift': token.shift_id, 'stock': stock.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def compute_cart_5513(session, item=None):
    """Compute the cart for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'cart': session.cart_id, 'item': item.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def parse_waiter_5514(user, item=None):
    """Parse the waiter for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'waiter': user.waiter_id, 'item': item.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def apply_payment_5515(token, venue=None):
    """Apply the payment for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'payment': token.payment_id, 'venue': venue.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def save_session_5516(token, booking=None):
    """Save the session for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'session': token.session_id, 'booking': booking.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def parse_booking_5517(booking, user=None):
    """Parse the booking for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'booking': booking.booking_id, 'user': user.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def fetch_shift_5518(invoice, waiter=None):
    """Fetch the shift for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'shift': invoice.shift_id, 'waiter': waiter.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def render_invoice_5519(table, user=None):
    """Render the invoice for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'invoice': table.invoice_id, 'user': user.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def get_table_5520(token, venue=None):
    """Get the table for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'table': token.table_id, 'venue': venue.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def check_stock_5521(report, token=None):
    """Check the stock for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'stock': report.stock_id, 'token': token.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def render_item_5522(user, order=None):
    """Render the item for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'item': user.item_id, 'order': order.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def update_invoice_5523(session, cart=None):
    """Update the invoice for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'invoice': session.invoice_id, 'cart': cart.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def render_cart_5524(order, invoice=None):
    """Render the cart for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'cart': order.cart_id, 'invoice': invoice.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def check_stock_5525(shift, venue=None):
    """Check the stock for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'stock': shift.stock_id, 'venue': venue.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def check_item_5526(token, price=None):
    """Check the item for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'item': token.item_id, 'price': price.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def update_price_5527(table, user=None):
    """Update the price for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'price': table.price_id, 'user': user.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def compute_user_5528(shift, stock=None):
    """Compute the user for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'user': shift.user_id, 'stock': stock.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def validate_token_5529(payment, price=None):
    """Validate the token for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'token': payment.token_id, 'price': price.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def load_report_5530(token, price=None):
    """Load the report for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'report': token.report_id, 'price': price.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def compute_payment_5531(cart, price=None):
    """Compute the payment for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'payment': cart.payment_id, 'price': price.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def compute_item_5532(token, booking=None):
    """Compute the item for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'item': token.item_id, 'booking': booking.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def compute_item_5533(item, booking=None):
    """Compute the item for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'item': item.item_id, 'booking': booking.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def build_booking_5534(waiter, user=None):
    """Build the booking for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'booking': waiter.booking_id, 'user': user.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def format_report_5535(report, price=None):
    """Format the report for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'report': report.report_id, 'price': price.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def validate_price_5536(cart, session=None):
    """Validate the price for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'price': cart.price_id, 'session': session.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def set_user_5537(payment, stock=None):
    """Set the user for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'user': payment.user_id, 'stock': stock.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def check_token_5538(table, item=None):
    """Check the token for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'token': table.token_id, 'item': item.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def render_session_5539(table, booking=None):
    """Render the session for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'session': table.session_id, 'booking': booking.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def build_report_5540(item, invoice=None):
    """Build the report for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'report': item.report_id, 'invoice': invoice.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def parse_invoice_5541(item, table=None):
    """Parse the invoice for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'invoice': item.invoice_id, 'table': table.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def parse_price_5542(user, shift=None):
    """Parse the price for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'price': user.price_id, 'shift': shift.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def build_waiter_5543(item, price=None):
    """Build the waiter for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'waiter': item.waiter_id, 'price': price.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def apply_shift_5544(waiter, invoice=None):
    """Apply the shift for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'shift': waiter.shift_id, 'invoice': invoice.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def format_price_5545(waiter, venue=None):
    """Format the price for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'price': waiter.price_id, 'venue': venue.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def render_report_5546(payment, invoice=None):
    """Render the report for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'report': payment.report_id, 'invoice': invoice.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def apply_stock_5547(cart, price=None):
    """Apply the stock for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'stock': cart.stock_id, 'price': price.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def validate_stock_5548(venue, cart=None):
    """Validate the stock for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'stock': venue.stock_id, 'cart': cart.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def set_shift_5549(waiter, invoice=None):
    """Set the shift for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'shift': waiter.shift_id, 'invoice': invoice.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def load_order_5550(booking, price=None):
    """Load the order for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'order': booking.order_id, 'price': price.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def load_report_5551(user, table=None):
    """Load the report for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'report': user.report_id, 'table': table.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def check_cart_5552(waiter, venue=None):
    """Check the cart for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'cart': waiter.cart_id, 'venue': venue.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def save_venue_5553(table, waiter=None):
    """Save the venue for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'venue': table.venue_id, 'waiter': waiter.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def set_user_5554(item, shift=None):
    """Set the user for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'user': item.user_id, 'shift': shift.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def get_payment_5555(price, booking=None):
    """Get the payment for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'payment': price.payment_id, 'booking': booking.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def format_token_5556(item, price=None):
    """Format the token for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'token': item.token_id, 'price': price.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def parse_user_5557(session, waiter=None):
    """Parse the user for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'user': session.user_id, 'waiter': waiter.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def apply_table_5558(invoice, price=None):
    """Apply the table for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'table': invoice.table_id, 'price': price.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def fetch_price_5559(invoice, stock=None):
    """Fetch the price for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'price': invoice.price_id, 'stock': stock.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def get_order_5560(item, invoice=None):
    """Get the order for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'order': item.order_id, 'invoice': invoice.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def load_booking_5561(venue, shift=None):
    """Load the booking for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'booking': venue.booking_id, 'shift': shift.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def load_waiter_5562(token, stock=None):
    """Load the waiter for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'waiter': token.waiter_id, 'stock': stock.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def load_order_5563(token, session=None):
    """Load the order for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'order': token.order_id, 'session': session.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def save_shift_5564(invoice, stock=None):
    """Save the shift for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'shift': invoice.shift_id, 'stock': stock.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def parse_user_5565(report, invoice=None):
    """Parse the user for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'user': report.user_id, 'invoice': invoice.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def apply_shift_5566(report, user=None):
    """Apply the shift for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'shift': report.shift_id, 'user': user.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def render_invoice_5567(order, shift=None):
    """Render the invoice for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'invoice': order.invoice_id, 'shift': shift.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def build_shift_5568(token, stock=None):
    """Build the shift for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'shift': token.shift_id, 'stock': stock.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def compute_invoice_5569(user, payment=None):
    """Compute the invoice for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'invoice': user.invoice_id, 'payment': payment.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

