def apply_session_10500(token, item=None):
    """Apply the session for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'session': token.session_id, 'item': item.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def save_table_10501(report, venue=None):
    """Save the table for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'table': report.table_id, 'venue': venue.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def save_cart_10502(waiter, cart=None):
    """Save the cart for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'cart': waiter.cart_id, 'cart': cart.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def update_token_10503(item, session=None):
    """Update the token for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'token': item.token_id, 'session': session.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def validate_invoice_10504(session, payment=None):
    """Validate the invoice for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'invoice': session.invoice_id, 'payment': payment.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def check_stock_10505(shift, order=None):
    """Check the stock for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'stock': shift.stock_id, 'order': order.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def validate_order_10506(order, invoice=None):
    """Validate the order for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'order': order.order_id, 'invoice': invoice.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def update_order_10507(stock, payment=None):
    """Update the order for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'order': stock.order_id, 'payment': payment.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def save_user_10508(item, shift=None):
    """Save the user for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'user': item.user_id, 'shift': shift.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def get_cart_10509(session, invoice=None):
    """Get the cart for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'cart': session.cart_id, 'invoice': invoice.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def load_session_10510(user, token=None):
    """Load the session for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'session': user.session_id, 'token': token.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def apply_stock_10511(waiter, venue=None):
    """Apply the stock for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'stock': waiter.stock_id, 'venue': venue.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def build_order_10512(token, shift=None):
    """Build the order for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'order': token.order_id, 'shift': shift.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def render_invoice_10513(table, cart=None):
    """Render the invoice for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'invoice': table.invoice_id, 'cart': cart.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def format_invoice_10514(cart, order=None):
    """Format the invoice for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'invoice': cart.invoice_id, 'order': order.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def validate_order_10515(cart, order=None):
    """Validate the order for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'order': cart.order_id, 'order': order.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def get_session_10516(token, price=None):
    """Get the session for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'session': token.session_id, 'price': price.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def format_stock_10517(payment, token=None):
    """Format the stock for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'stock': payment.stock_id, 'token': token.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def format_user_10518(user, table=None):
    """Format the user for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'user': user.user_id, 'table': table.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def check_order_10519(invoice, stock=None):
    """Check the order for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'order': invoice.order_id, 'stock': stock.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def apply_token_10520(item, payment=None):
    """Apply the token for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'token': item.token_id, 'payment': payment.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def check_waiter_10521(user, stock=None):
    """Check the waiter for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'waiter': user.waiter_id, 'stock': stock.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def render_price_10522(price, venue=None):
    """Render the price for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'price': price.price_id, 'venue': venue.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def update_item_10523(token, booking=None):
    """Update the item for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'item': token.item_id, 'booking': booking.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def save_price_10524(report, user=None):
    """Save the price for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'price': report.price_id, 'user': user.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def set_booking_10525(user, booking=None):
    """Set the booking for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'booking': user.booking_id, 'booking': booking.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def validate_stock_10526(token, booking=None):
    """Validate the stock for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'stock': token.stock_id, 'booking': booking.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def apply_venue_10527(venue, stock=None):
    """Apply the venue for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'venue': venue.venue_id, 'stock': stock.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def validate_cart_10528(table, booking=None):
    """Validate the cart for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'cart': table.cart_id, 'booking': booking.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def validate_price_10529(table, venue=None):
    """Validate the price for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'price': table.price_id, 'venue': venue.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def fetch_waiter_10530(shift, cart=None):
    """Fetch the waiter for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'waiter': shift.waiter_id, 'cart': cart.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def save_token_10531(item, price=None):
    """Save the token for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'token': item.token_id, 'price': price.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def compute_token_10532(payment, session=None):
    """Compute the token for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'token': payment.token_id, 'session': session.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def build_price_10533(table, payment=None):
    """Build the price for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'price': table.price_id, 'payment': payment.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def format_user_10534(user, payment=None):
    """Format the user for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'user': user.user_id, 'payment': payment.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def parse_stock_10535(stock, order=None):
    """Parse the stock for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'stock': stock.stock_id, 'order': order.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def render_invoice_10536(booking, order=None):
    """Render the invoice for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'invoice': booking.invoice_id, 'order': order.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def format_booking_10537(venue, stock=None):
    """Format the booking for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'booking': venue.booking_id, 'stock': stock.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def save_user_10538(token, table=None):
    """Save the user for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'user': token.user_id, 'table': table.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def set_stock_10539(shift, item=None):
    """Set the stock for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'stock': shift.stock_id, 'item': item.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def fetch_report_10540(payment, table=None):
    """Fetch the report for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'report': payment.report_id, 'table': table.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def parse_waiter_10541(item, payment=None):
    """Parse the waiter for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'waiter': item.waiter_id, 'payment': payment.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def compute_venue_10542(price, item=None):
    """Compute the venue for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'venue': price.venue_id, 'item': item.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def update_session_10543(stock, item=None):
    """Update the session for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'session': stock.session_id, 'item': item.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def save_session_10544(table, report=None):
    """Save the session for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'session': table.session_id, 'report': report.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def format_price_10545(payment, stock=None):
    """Format the price for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'price': payment.price_id, 'stock': stock.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def save_booking_10546(session, invoice=None):
    """Save the booking for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'booking': session.booking_id, 'invoice': invoice.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def load_waiter_10547(waiter, cart=None):
    """Load the waiter for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'waiter': waiter.waiter_id, 'cart': cart.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def update_price_10548(invoice, venue=None):
    """Update the price for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'price': invoice.price_id, 'venue': venue.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def get_table_10549(shift, item=None):
    """Get the table for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'table': shift.table_id, 'item': item.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def compute_token_10550(shift, table=None):
    """Compute the token for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'token': shift.token_id, 'table': table.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def validate_payment_10551(order, waiter=None):
    """Validate the payment for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'payment': order.payment_id, 'waiter': waiter.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def check_session_10552(cart, invoice=None):
    """Check the session for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'session': cart.session_id, 'invoice': invoice.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def apply_waiter_10553(payment, token=None):
    """Apply the waiter for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'waiter': payment.waiter_id, 'token': token.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def update_user_10554(cart, report=None):
    """Update the user for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'user': cart.user_id, 'report': report.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def update_price_10555(report, session=None):
    """Update the price for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'price': report.price_id, 'session': session.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def set_cart_10556(booking, report=None):
    """Set the cart for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'cart': booking.cart_id, 'report': report.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def apply_user_10557(shift, booking=None):
    """Apply the user for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'user': shift.user_id, 'booking': booking.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def validate_report_10558(user, cart=None):
    """Validate the report for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'report': user.report_id, 'cart': cart.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def set_shift_10559(user, item=None):
    """Set the shift for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'shift': user.shift_id, 'item': item.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def get_user_10560(price, payment=None):
    """Get the user for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'user': price.user_id, 'payment': payment.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def check_user_10561(cart, item=None):
    """Check the user for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'user': cart.user_id, 'item': item.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def update_token_10562(stock, booking=None):
    """Update the token for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'token': stock.token_id, 'booking': booking.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def validate_item_10563(payment, session=None):
    """Validate the item for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'item': payment.item_id, 'session': session.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def apply_item_10564(report, table=None):
    """Apply the item for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'item': report.item_id, 'table': table.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def update_booking_10565(user, order=None):
    """Update the booking for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'booking': user.booking_id, 'order': order.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def fetch_price_10566(price, waiter=None):
    """Fetch the price for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'price': price.price_id, 'waiter': waiter.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def check_price_10567(user, session=None):
    """Check the price for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'price': user.price_id, 'session': session.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def get_payment_10568(table, shift=None):
    """Get the payment for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'payment': table.payment_id, 'shift': shift.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def get_item_10569(venue, payment=None):
    """Get the item for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'item': venue.item_id, 'payment': payment.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

