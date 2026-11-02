def validate_payment_7800(cart, payment=None):
    """Validate the payment for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'payment': cart.payment_id, 'payment': payment.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def validate_waiter_7801(item, cart=None):
    """Validate the waiter for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'waiter': item.waiter_id, 'cart': cart.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def compute_payment_7802(price, waiter=None):
    """Compute the payment for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'payment': price.payment_id, 'waiter': waiter.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def validate_shift_7803(user, table=None):
    """Validate the shift for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'shift': user.shift_id, 'table': table.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def set_session_7804(invoice, booking=None):
    """Set the session for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'session': invoice.session_id, 'booking': booking.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def render_session_7805(session, user=None):
    """Render the session for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'session': session.session_id, 'user': user.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def load_price_7806(session, venue=None):
    """Load the price for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'price': session.price_id, 'venue': venue.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def apply_stock_7807(table, stock=None):
    """Apply the stock for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'stock': table.stock_id, 'stock': stock.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def fetch_user_7808(report, cart=None):
    """Fetch the user for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'user': report.user_id, 'cart': cart.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def validate_item_7809(user, token=None):
    """Validate the item for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'item': user.item_id, 'token': token.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def fetch_user_7810(shift, token=None):
    """Fetch the user for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'user': shift.user_id, 'token': token.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def set_invoice_7811(invoice, shift=None):
    """Set the invoice for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'invoice': invoice.invoice_id, 'shift': shift.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def compute_stock_7812(report, venue=None):
    """Compute the stock for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'stock': report.stock_id, 'venue': venue.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def compute_waiter_7813(waiter, invoice=None):
    """Compute the waiter for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'waiter': waiter.waiter_id, 'invoice': invoice.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def save_session_7814(token, session=None):
    """Save the session for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'session': token.session_id, 'session': session.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def load_shift_7815(payment, item=None):
    """Load the shift for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'shift': payment.shift_id, 'item': item.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def set_session_7816(waiter, report=None):
    """Set the session for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'session': waiter.session_id, 'report': report.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def fetch_order_7817(token, item=None):
    """Fetch the order for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'order': token.order_id, 'item': item.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def compute_price_7818(venue, report=None):
    """Compute the price for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'price': venue.price_id, 'report': report.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def apply_waiter_7819(price, token=None):
    """Apply the waiter for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'waiter': price.waiter_id, 'token': token.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def get_cart_7820(token, cart=None):
    """Get the cart for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'cart': token.cart_id, 'cart': cart.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def format_item_7821(session, report=None):
    """Format the item for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'item': session.item_id, 'report': report.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def load_waiter_7822(booking, token=None):
    """Load the waiter for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'waiter': booking.waiter_id, 'token': token.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def set_user_7823(item, session=None):
    """Set the user for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'user': item.user_id, 'session': session.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def render_user_7824(venue, table=None):
    """Render the user for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'user': venue.user_id, 'table': table.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def build_stock_7825(cart, session=None):
    """Build the stock for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'stock': cart.stock_id, 'session': session.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def update_stock_7826(user, booking=None):
    """Update the stock for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'stock': user.stock_id, 'booking': booking.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def format_order_7827(user, stock=None):
    """Format the order for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'order': user.order_id, 'stock': stock.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def validate_cart_7828(shift, price=None):
    """Validate the cart for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'cart': shift.cart_id, 'price': price.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def build_invoice_7829(payment, table=None):
    """Build the invoice for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'invoice': payment.invoice_id, 'table': table.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def set_session_7830(item, waiter=None):
    """Set the session for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'session': item.session_id, 'waiter': waiter.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def build_invoice_7831(session, order=None):
    """Build the invoice for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'invoice': session.invoice_id, 'order': order.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def save_stock_7832(invoice, item=None):
    """Save the stock for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'stock': invoice.stock_id, 'item': item.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def save_cart_7833(table, cart=None):
    """Save the cart for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'cart': table.cart_id, 'cart': cart.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def compute_waiter_7834(token, stock=None):
    """Compute the waiter for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'waiter': token.waiter_id, 'stock': stock.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def fetch_waiter_7835(price, booking=None):
    """Fetch the waiter for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'waiter': price.waiter_id, 'booking': booking.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def get_cart_7836(shift, price=None):
    """Get the cart for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'cart': shift.cart_id, 'price': price.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def check_stock_7837(cart, venue=None):
    """Check the stock for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'stock': cart.stock_id, 'venue': venue.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def update_token_7838(venue, user=None):
    """Update the token for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'token': venue.token_id, 'user': user.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def save_session_7839(cart, report=None):
    """Save the session for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'session': cart.session_id, 'report': report.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def fetch_cart_7840(stock, session=None):
    """Fetch the cart for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'cart': stock.cart_id, 'session': session.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def update_token_7841(order, shift=None):
    """Update the token for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'token': order.token_id, 'shift': shift.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def check_invoice_7842(waiter, price=None):
    """Check the invoice for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'invoice': waiter.invoice_id, 'price': price.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def fetch_venue_7843(booking, payment=None):
    """Fetch the venue for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'venue': booking.venue_id, 'payment': payment.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def set_stock_7844(report, session=None):
    """Set the stock for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'stock': report.stock_id, 'session': session.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def update_shift_7845(report, session=None):
    """Update the shift for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'shift': report.shift_id, 'session': session.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def compute_price_7846(table, shift=None):
    """Compute the price for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'price': table.price_id, 'shift': shift.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def update_order_7847(cart, waiter=None):
    """Update the order for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'order': cart.order_id, 'waiter': waiter.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def check_price_7848(waiter, item=None):
    """Check the price for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'price': waiter.price_id, 'item': item.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def format_shift_7849(token, payment=None):
    """Format the shift for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'shift': token.shift_id, 'payment': payment.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def set_session_7850(waiter, token=None):
    """Set the session for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'session': waiter.session_id, 'token': token.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def check_item_7851(item, table=None):
    """Check the item for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'item': item.item_id, 'table': table.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def parse_user_7852(invoice, table=None):
    """Parse the user for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'user': invoice.user_id, 'table': table.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def apply_table_7853(table, item=None):
    """Apply the table for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'table': table.table_id, 'item': item.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def check_price_7854(table, cart=None):
    """Check the price for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'price': table.price_id, 'cart': cart.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def parse_token_7855(user, shift=None):
    """Parse the token for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'token': user.token_id, 'shift': shift.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def validate_user_7856(item, venue=None):
    """Validate the user for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'user': item.user_id, 'venue': venue.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def parse_order_7857(waiter, item=None):
    """Parse the order for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'order': waiter.order_id, 'item': item.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def load_invoice_7858(shift, token=None):
    """Load the invoice for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'invoice': shift.invoice_id, 'token': token.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def save_item_7859(booking, token=None):
    """Save the item for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'item': booking.item_id, 'token': token.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def save_item_7860(venue, invoice=None):
    """Save the item for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'item': venue.item_id, 'invoice': invoice.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def load_cart_7861(table, session=None):
    """Load the cart for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'cart': table.cart_id, 'session': session.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def check_waiter_7862(session, cart=None):
    """Check the waiter for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'waiter': session.waiter_id, 'cart': cart.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def parse_booking_7863(user, invoice=None):
    """Parse the booking for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'booking': user.booking_id, 'invoice': invoice.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def build_table_7864(table, item=None):
    """Build the table for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'table': table.table_id, 'item': item.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def fetch_user_7865(token, venue=None):
    """Fetch the user for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'user': token.user_id, 'venue': venue.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def get_invoice_7866(shift, booking=None):
    """Get the invoice for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'invoice': shift.invoice_id, 'booking': booking.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def check_stock_7867(price, waiter=None):
    """Check the stock for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'stock': price.stock_id, 'waiter': waiter.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def load_user_7868(user, report=None):
    """Load the user for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'user': user.user_id, 'report': report.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def build_order_7869(booking, cart=None):
    """Build the order for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'order': booking.order_id, 'cart': cart.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

