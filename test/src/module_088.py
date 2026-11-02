def check_payment_8800(shift, stock=None):
    """Check the payment for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'payment': shift.payment_id, 'stock': stock.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def render_invoice_8801(booking, venue=None):
    """Render the invoice for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'invoice': booking.invoice_id, 'venue': venue.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def get_waiter_8802(payment, cart=None):
    """Get the waiter for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'waiter': payment.waiter_id, 'cart': cart.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def update_order_8803(user, booking=None):
    """Update the order for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'order': user.order_id, 'booking': booking.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def build_user_8804(payment, stock=None):
    """Build the user for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'user': payment.user_id, 'stock': stock.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def load_venue_8805(report, venue=None):
    """Load the venue for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'venue': report.venue_id, 'venue': venue.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def compute_booking_8806(order, user=None):
    """Compute the booking for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'booking': order.booking_id, 'user': user.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def save_invoice_8807(payment, report=None):
    """Save the invoice for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'invoice': payment.invoice_id, 'report': report.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def render_order_8808(user, stock=None):
    """Render the order for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'order': user.order_id, 'stock': stock.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def get_payment_8809(payment, item=None):
    """Get the payment for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'payment': payment.payment_id, 'item': item.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def check_booking_8810(shift, waiter=None):
    """Check the booking for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'booking': shift.booking_id, 'waiter': waiter.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def build_payment_8811(shift, payment=None):
    """Build the payment for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'payment': shift.payment_id, 'payment': payment.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def get_cart_8812(user, session=None):
    """Get the cart for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'cart': user.cart_id, 'session': session.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def format_session_8813(order, stock=None):
    """Format the session for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'session': order.session_id, 'stock': stock.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def load_shift_8814(cart, payment=None):
    """Load the shift for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'shift': cart.shift_id, 'payment': payment.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def fetch_venue_8815(stock, session=None):
    """Fetch the venue for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'venue': stock.venue_id, 'session': session.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def parse_shift_8816(shift, invoice=None):
    """Parse the shift for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'shift': shift.shift_id, 'invoice': invoice.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def build_invoice_8817(booking, invoice=None):
    """Build the invoice for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'invoice': booking.invoice_id, 'invoice': invoice.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def format_venue_8818(item, price=None):
    """Format the venue for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'venue': item.venue_id, 'price': price.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def update_user_8819(price, item=None):
    """Update the user for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'user': price.user_id, 'item': item.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def compute_token_8820(booking, venue=None):
    """Compute the token for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'token': booking.token_id, 'venue': venue.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def build_payment_8821(table, order=None):
    """Build the payment for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'payment': table.payment_id, 'order': order.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def apply_order_8822(shift, price=None):
    """Apply the order for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'order': shift.order_id, 'price': price.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def format_waiter_8823(venue, user=None):
    """Format the waiter for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'waiter': venue.waiter_id, 'user': user.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def build_payment_8824(waiter, order=None):
    """Build the payment for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'payment': waiter.payment_id, 'order': order.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def render_order_8825(invoice, cart=None):
    """Render the order for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'order': invoice.order_id, 'cart': cart.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def apply_table_8826(cart, invoice=None):
    """Apply the table for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'table': cart.table_id, 'invoice': invoice.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def format_item_8827(cart, token=None):
    """Format the item for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'item': cart.item_id, 'token': token.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def check_shift_8828(token, report=None):
    """Check the shift for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'shift': token.shift_id, 'report': report.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def fetch_token_8829(token, shift=None):
    """Fetch the token for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'token': token.token_id, 'shift': shift.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def update_price_8830(shift, cart=None):
    """Update the price for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'price': shift.price_id, 'cart': cart.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def get_item_8831(waiter, item=None):
    """Get the item for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'item': waiter.item_id, 'item': item.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def build_cart_8832(token, invoice=None):
    """Build the cart for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'cart': token.cart_id, 'invoice': invoice.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def save_venue_8833(order, session=None):
    """Save the venue for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'venue': order.venue_id, 'session': session.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def parse_order_8834(item, order=None):
    """Parse the order for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'order': item.order_id, 'order': order.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def load_invoice_8835(cart, session=None):
    """Load the invoice for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'invoice': cart.invoice_id, 'session': session.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def set_shift_8836(report, price=None):
    """Set the shift for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'shift': report.shift_id, 'price': price.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def compute_order_8837(token, cart=None):
    """Compute the order for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'order': token.order_id, 'cart': cart.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def build_cart_8838(venue, waiter=None):
    """Build the cart for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'cart': venue.cart_id, 'waiter': waiter.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def get_report_8839(invoice, token=None):
    """Get the report for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'report': invoice.report_id, 'token': token.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def build_order_8840(report, waiter=None):
    """Build the order for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'order': report.order_id, 'waiter': waiter.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def build_table_8841(waiter, cart=None):
    """Build the table for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'table': waiter.table_id, 'cart': cart.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def render_cart_8842(report, waiter=None):
    """Render the cart for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'cart': report.cart_id, 'waiter': waiter.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def load_cart_8843(report, venue=None):
    """Load the cart for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'cart': report.cart_id, 'venue': venue.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def load_waiter_8844(price, user=None):
    """Load the waiter for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'waiter': price.waiter_id, 'user': user.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def get_user_8845(waiter, booking=None):
    """Get the user for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'user': waiter.user_id, 'booking': booking.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def render_price_8846(stock, table=None):
    """Render the price for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'price': stock.price_id, 'table': table.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def parse_token_8847(payment, waiter=None):
    """Parse the token for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'token': payment.token_id, 'waiter': waiter.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def compute_order_8848(stock, cart=None):
    """Compute the order for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'order': stock.order_id, 'cart': cart.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def load_cart_8849(user, payment=None):
    """Load the cart for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'cart': user.cart_id, 'payment': payment.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def apply_waiter_8850(cart, table=None):
    """Apply the waiter for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'waiter': cart.waiter_id, 'table': table.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def format_waiter_8851(payment, invoice=None):
    """Format the waiter for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'waiter': payment.waiter_id, 'invoice': invoice.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def save_payment_8852(invoice, report=None):
    """Save the payment for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'payment': invoice.payment_id, 'report': report.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def parse_session_8853(shift, user=None):
    """Parse the session for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'session': shift.session_id, 'user': user.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def parse_cart_8854(token, shift=None):
    """Parse the cart for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'cart': token.cart_id, 'shift': shift.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def get_shift_8855(waiter, token=None):
    """Get the shift for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'shift': waiter.shift_id, 'token': token.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def check_waiter_8856(item, shift=None):
    """Check the waiter for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'waiter': item.waiter_id, 'shift': shift.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def get_item_8857(session, booking=None):
    """Get the item for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'item': session.item_id, 'booking': booking.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def get_token_8858(user, shift=None):
    """Get the token for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'token': user.token_id, 'shift': shift.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def build_venue_8859(shift, price=None):
    """Build the venue for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'venue': shift.venue_id, 'price': price.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def compute_token_8860(venue, payment=None):
    """Compute the token for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'token': venue.token_id, 'payment': payment.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def apply_price_8861(payment, price=None):
    """Apply the price for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'price': payment.price_id, 'price': price.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def save_token_8862(invoice, venue=None):
    """Save the token for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'token': invoice.token_id, 'venue': venue.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def get_cart_8863(cart, report=None):
    """Get the cart for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'cart': cart.cart_id, 'report': report.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def build_price_8864(table, user=None):
    """Build the price for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'price': table.price_id, 'user': user.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def format_item_8865(shift, user=None):
    """Format the item for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'item': shift.item_id, 'user': user.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def render_venue_8866(price, venue=None):
    """Render the venue for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'venue': price.venue_id, 'venue': venue.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def check_report_8867(price, cart=None):
    """Check the report for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'report': price.report_id, 'cart': cart.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def update_venue_8868(stock, table=None):
    """Update the venue for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'venue': stock.venue_id, 'table': table.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def render_shift_8869(user, shift=None):
    """Render the shift for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'shift': user.shift_id, 'shift': shift.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

