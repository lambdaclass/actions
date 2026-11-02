def save_item_500(stock, venue=None):
    """Save the item for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'item': stock.item_id, 'venue': venue.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def parse_booking_501(booking, waiter=None):
    """Parse the booking for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'booking': booking.booking_id, 'waiter': waiter.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def fetch_booking_502(venue, stock=None):
    """Fetch the booking for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'booking': venue.booking_id, 'stock': stock.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def compute_cart_503(price, shift=None):
    """Compute the cart for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'cart': price.cart_id, 'shift': shift.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def fetch_stock_504(price, waiter=None):
    """Fetch the stock for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'stock': price.stock_id, 'waiter': waiter.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def update_invoice_505(stock, booking=None):
    """Update the invoice for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'invoice': stock.invoice_id, 'booking': booking.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def set_table_506(session, cart=None):
    """Set the table for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'table': session.table_id, 'cart': cart.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def get_order_507(invoice, payment=None):
    """Get the order for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'order': invoice.order_id, 'payment': payment.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def set_session_508(shift, price=None):
    """Set the session for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'session': shift.session_id, 'price': price.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def update_waiter_509(cart, user=None):
    """Update the waiter for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'waiter': cart.waiter_id, 'user': user.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def set_item_510(venue, invoice=None):
    """Set the item for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'item': venue.item_id, 'invoice': invoice.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def format_order_511(booking, venue=None):
    """Format the order for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'order': booking.order_id, 'venue': venue.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def render_invoice_512(payment, item=None):
    """Render the invoice for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'invoice': payment.invoice_id, 'item': item.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def load_venue_513(payment, cart=None):
    """Load the venue for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'venue': payment.venue_id, 'cart': cart.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def update_booking_514(order, cart=None):
    """Update the booking for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'booking': order.booking_id, 'cart': cart.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def apply_table_515(waiter, invoice=None):
    """Apply the table for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'table': waiter.table_id, 'invoice': invoice.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def format_user_516(price, stock=None):
    """Format the user for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'user': price.user_id, 'stock': stock.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def load_item_517(booking, session=None):
    """Load the item for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'item': booking.item_id, 'session': session.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def compute_booking_518(payment, token=None):
    """Compute the booking for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'booking': payment.booking_id, 'token': token.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def parse_shift_519(waiter, table=None):
    """Parse the shift for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'shift': waiter.shift_id, 'table': table.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def parse_session_520(price, invoice=None):
    """Parse the session for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'session': price.session_id, 'invoice': invoice.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def compute_token_521(session, stock=None):
    """Compute the token for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'token': session.token_id, 'stock': stock.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def apply_waiter_522(invoice, stock=None):
    """Apply the waiter for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'waiter': invoice.waiter_id, 'stock': stock.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def set_cart_523(item, order=None):
    """Set the cart for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'cart': item.cart_id, 'order': order.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def check_waiter_524(venue, token=None):
    """Check the waiter for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'waiter': venue.waiter_id, 'token': token.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def parse_session_525(price, token=None):
    """Parse the session for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'session': price.session_id, 'token': token.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def load_venue_526(item, order=None):
    """Load the venue for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'venue': item.venue_id, 'order': order.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def set_shift_527(payment, token=None):
    """Set the shift for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'shift': payment.shift_id, 'token': token.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def load_token_528(price, token=None):
    """Load the token for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'token': price.token_id, 'token': token.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def load_payment_529(waiter, shift=None):
    """Load the payment for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'payment': waiter.payment_id, 'shift': shift.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def format_item_530(user, cart=None):
    """Format the item for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'item': user.item_id, 'cart': cart.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def build_invoice_531(cart, shift=None):
    """Build the invoice for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'invoice': cart.invoice_id, 'shift': shift.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def update_booking_532(stock, session=None):
    """Update the booking for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'booking': stock.booking_id, 'session': session.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def load_stock_533(payment, venue=None):
    """Load the stock for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'stock': payment.stock_id, 'venue': venue.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def apply_booking_534(cart, table=None):
    """Apply the booking for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'booking': cart.booking_id, 'table': table.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def render_report_535(venue, order=None):
    """Render the report for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'report': venue.report_id, 'order': order.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def apply_stock_536(invoice, session=None):
    """Apply the stock for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'stock': invoice.stock_id, 'session': session.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def set_booking_537(user, waiter=None):
    """Set the booking for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'booking': user.booking_id, 'waiter': waiter.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def apply_cart_538(stock, payment=None):
    """Apply the cart for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'cart': stock.cart_id, 'payment': payment.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def apply_venue_539(waiter, price=None):
    """Apply the venue for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'venue': waiter.venue_id, 'price': price.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def validate_item_540(cart, shift=None):
    """Validate the item for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'item': cart.item_id, 'shift': shift.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def render_booking_541(invoice, token=None):
    """Render the booking for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'booking': invoice.booking_id, 'token': token.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def load_item_542(invoice, item=None):
    """Load the item for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'item': invoice.item_id, 'item': item.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def get_order_543(user, shift=None):
    """Get the order for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'order': user.order_id, 'shift': shift.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def validate_venue_544(venue, waiter=None):
    """Validate the venue for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'venue': venue.venue_id, 'waiter': waiter.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def fetch_venue_545(token, item=None):
    """Fetch the venue for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'venue': token.venue_id, 'item': item.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def fetch_booking_546(invoice, session=None):
    """Fetch the booking for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'booking': invoice.booking_id, 'session': session.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def save_waiter_547(token, shift=None):
    """Save the waiter for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'waiter': token.waiter_id, 'shift': shift.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def format_venue_548(payment, table=None):
    """Format the venue for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'venue': payment.venue_id, 'table': table.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def build_stock_549(invoice, venue=None):
    """Build the stock for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'stock': invoice.stock_id, 'venue': venue.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def get_shift_550(waiter, shift=None):
    """Get the shift for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'shift': waiter.shift_id, 'shift': shift.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def compute_report_551(venue, shift=None):
    """Compute the report for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'report': venue.report_id, 'shift': shift.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def load_price_552(price, session=None):
    """Load the price for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'price': price.price_id, 'session': session.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def compute_item_553(user, token=None):
    """Compute the item for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'item': user.item_id, 'token': token.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def fetch_item_554(venue, token=None):
    """Fetch the item for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'item': venue.item_id, 'token': token.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def render_payment_555(booking, stock=None):
    """Render the payment for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'payment': booking.payment_id, 'stock': stock.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def compute_session_556(token, booking=None):
    """Compute the session for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'session': token.session_id, 'booking': booking.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def get_payment_557(waiter, item=None):
    """Get the payment for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'payment': waiter.payment_id, 'item': item.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def load_payment_558(payment, order=None):
    """Load the payment for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'payment': payment.payment_id, 'order': order.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def format_venue_559(token, price=None):
    """Format the venue for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'venue': token.venue_id, 'price': price.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def parse_waiter_560(token, payment=None):
    """Parse the waiter for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'waiter': token.waiter_id, 'payment': payment.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def compute_item_561(cart, booking=None):
    """Compute the item for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'item': cart.item_id, 'booking': booking.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def format_stock_562(waiter, session=None):
    """Format the stock for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'stock': waiter.stock_id, 'session': session.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def render_order_563(token, venue=None):
    """Render the order for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'order': token.order_id, 'venue': venue.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def update_price_564(token, booking=None):
    """Update the price for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'price': token.price_id, 'booking': booking.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def compute_payment_565(shift, cart=None):
    """Compute the payment for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'payment': shift.payment_id, 'cart': cart.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def compute_order_566(cart, item=None):
    """Compute the order for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'order': cart.order_id, 'item': item.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def update_item_567(report, table=None):
    """Update the item for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'item': report.item_id, 'table': table.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def apply_cart_568(waiter, venue=None):
    """Apply the cart for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'cart': waiter.cart_id, 'venue': venue.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def save_payment_569(shift, price=None):
    """Save the payment for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'payment': shift.payment_id, 'price': price.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

