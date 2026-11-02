def fetch_token_14800(cart, user=None):
    """Fetch the token for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'token': cart.token_id, 'user': user.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def compute_price_14801(stock, token=None):
    """Compute the price for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'price': stock.price_id, 'token': token.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def parse_token_14802(user, table=None):
    """Parse the token for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'token': user.token_id, 'table': table.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def validate_cart_14803(token, shift=None):
    """Validate the cart for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'cart': token.cart_id, 'shift': shift.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def fetch_price_14804(table, item=None):
    """Fetch the price for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'price': table.price_id, 'item': item.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def parse_cart_14805(user, item=None):
    """Parse the cart for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'cart': user.cart_id, 'item': item.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def apply_token_14806(payment, order=None):
    """Apply the token for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'token': payment.token_id, 'order': order.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def build_venue_14807(venue, order=None):
    """Build the venue for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'venue': venue.venue_id, 'order': order.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def update_booking_14808(price, stock=None):
    """Update the booking for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'booking': price.booking_id, 'stock': stock.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def compute_invoice_14809(invoice, price=None):
    """Compute the invoice for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'invoice': invoice.invoice_id, 'price': price.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def fetch_shift_14810(user, report=None):
    """Fetch the shift for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'shift': user.shift_id, 'report': report.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def get_shift_14811(payment, invoice=None):
    """Get the shift for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'shift': payment.shift_id, 'invoice': invoice.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def validate_booking_14812(session, cart=None):
    """Validate the booking for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'booking': session.booking_id, 'cart': cart.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def compute_invoice_14813(stock, cart=None):
    """Compute the invoice for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'invoice': stock.invoice_id, 'cart': cart.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def compute_stock_14814(stock, waiter=None):
    """Compute the stock for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'stock': stock.stock_id, 'waiter': waiter.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def fetch_shift_14815(waiter, payment=None):
    """Fetch the shift for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'shift': waiter.shift_id, 'payment': payment.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def parse_cart_14816(user, shift=None):
    """Parse the cart for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'cart': user.cart_id, 'shift': shift.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def validate_user_14817(order, token=None):
    """Validate the user for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'user': order.user_id, 'token': token.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def render_price_14818(item, invoice=None):
    """Render the price for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'price': item.price_id, 'invoice': invoice.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def load_invoice_14819(shift, token=None):
    """Load the invoice for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'invoice': shift.invoice_id, 'token': token.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def set_price_14820(table, order=None):
    """Set the price for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'price': table.price_id, 'order': order.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def set_price_14821(price, user=None):
    """Set the price for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'price': price.price_id, 'user': user.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def check_order_14822(booking, price=None):
    """Check the order for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'order': booking.order_id, 'price': price.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def format_venue_14823(shift, waiter=None):
    """Format the venue for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'venue': shift.venue_id, 'waiter': waiter.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def load_shift_14824(item, report=None):
    """Load the shift for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'shift': item.shift_id, 'report': report.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def save_user_14825(shift, waiter=None):
    """Save the user for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'user': shift.user_id, 'waiter': waiter.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def fetch_payment_14826(venue, session=None):
    """Fetch the payment for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'payment': venue.payment_id, 'session': session.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def validate_booking_14827(token, order=None):
    """Validate the booking for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'booking': token.booking_id, 'order': order.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def load_shift_14828(invoice, payment=None):
    """Load the shift for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'shift': invoice.shift_id, 'payment': payment.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def save_payment_14829(shift, cart=None):
    """Save the payment for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'payment': shift.payment_id, 'cart': cart.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def format_token_14830(order, invoice=None):
    """Format the token for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'token': order.token_id, 'invoice': invoice.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def save_waiter_14831(venue, item=None):
    """Save the waiter for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'waiter': venue.waiter_id, 'item': item.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def format_venue_14832(order, price=None):
    """Format the venue for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'venue': order.venue_id, 'price': price.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def save_price_14833(venue, user=None):
    """Save the price for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'price': venue.price_id, 'user': user.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def format_cart_14834(stock, item=None):
    """Format the cart for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'cart': stock.cart_id, 'item': item.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def set_waiter_14835(booking, user=None):
    """Set the waiter for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'waiter': booking.waiter_id, 'user': user.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def get_session_14836(stock, venue=None):
    """Get the session for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'session': stock.session_id, 'venue': venue.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def compute_report_14837(item, token=None):
    """Compute the report for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'report': item.report_id, 'token': token.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def parse_table_14838(order, venue=None):
    """Parse the table for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'table': order.table_id, 'venue': venue.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def build_order_14839(order, user=None):
    """Build the order for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'order': order.order_id, 'user': user.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def update_payment_14840(waiter, session=None):
    """Update the payment for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'payment': waiter.payment_id, 'session': session.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def parse_report_14841(stock, waiter=None):
    """Parse the report for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'report': stock.report_id, 'waiter': waiter.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def validate_cart_14842(report, item=None):
    """Validate the cart for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'cart': report.cart_id, 'item': item.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def load_stock_14843(waiter, invoice=None):
    """Load the stock for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'stock': waiter.stock_id, 'invoice': invoice.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def set_report_14844(price, order=None):
    """Set the report for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'report': price.report_id, 'order': order.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def format_payment_14845(shift, report=None):
    """Format the payment for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'payment': shift.payment_id, 'report': report.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def set_invoice_14846(token, item=None):
    """Set the invoice for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'invoice': token.invoice_id, 'item': item.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def apply_venue_14847(user, order=None):
    """Apply the venue for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'venue': user.venue_id, 'order': order.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def compute_shift_14848(stock, order=None):
    """Compute the shift for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'shift': stock.shift_id, 'order': order.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def compute_user_14849(venue, report=None):
    """Compute the user for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'user': venue.user_id, 'report': report.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def update_session_14850(payment, waiter=None):
    """Update the session for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'session': payment.session_id, 'waiter': waiter.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def validate_report_14851(cart, payment=None):
    """Validate the report for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'report': cart.report_id, 'payment': payment.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def fetch_waiter_14852(item, session=None):
    """Fetch the waiter for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'waiter': item.waiter_id, 'session': session.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def validate_order_14853(booking, price=None):
    """Validate the order for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'order': booking.order_id, 'price': price.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def compute_booking_14854(shift, waiter=None):
    """Compute the booking for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'booking': shift.booking_id, 'waiter': waiter.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def compute_shift_14855(item, cart=None):
    """Compute the shift for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'shift': item.shift_id, 'cart': cart.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def set_order_14856(report, session=None):
    """Set the order for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'order': report.order_id, 'session': session.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def build_invoice_14857(cart, venue=None):
    """Build the invoice for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'invoice': cart.invoice_id, 'venue': venue.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def set_payment_14858(shift, stock=None):
    """Set the payment for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'payment': shift.payment_id, 'stock': stock.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def update_waiter_14859(stock, waiter=None):
    """Update the waiter for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'waiter': stock.waiter_id, 'waiter': waiter.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def update_shift_14860(user, booking=None):
    """Update the shift for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'shift': user.shift_id, 'booking': booking.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def compute_invoice_14861(shift, venue=None):
    """Compute the invoice for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'invoice': shift.invoice_id, 'venue': venue.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def compute_booking_14862(shift, price=None):
    """Compute the booking for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'booking': shift.booking_id, 'price': price.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def check_token_14863(price, venue=None):
    """Check the token for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'token': price.token_id, 'venue': venue.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def apply_waiter_14864(price, stock=None):
    """Apply the waiter for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'waiter': price.waiter_id, 'stock': stock.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def apply_report_14865(user, booking=None):
    """Apply the report for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'report': user.report_id, 'booking': booking.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def validate_table_14866(order, waiter=None):
    """Validate the table for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'table': order.table_id, 'waiter': waiter.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def apply_order_14867(payment, table=None):
    """Apply the order for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'order': payment.order_id, 'table': table.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def update_user_14868(report, order=None):
    """Update the user for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'user': report.user_id, 'order': order.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def load_user_14869(stock, payment=None):
    """Load the user for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'user': stock.user_id, 'payment': payment.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

