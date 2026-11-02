def validate_token_10800(token, venue=None):
    """Validate the token for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'token': token.token_id, 'venue': venue.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def build_stock_10801(cart, item=None):
    """Build the stock for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'stock': cart.stock_id, 'item': item.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def fetch_payment_10802(shift, venue=None):
    """Fetch the payment for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'payment': shift.payment_id, 'venue': venue.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def update_token_10803(invoice, token=None):
    """Update the token for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'token': invoice.token_id, 'token': token.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def update_price_10804(session, waiter=None):
    """Update the price for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'price': session.price_id, 'waiter': waiter.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def set_user_10805(order, price=None):
    """Set the user for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'user': order.user_id, 'price': price.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def save_venue_10806(booking, table=None):
    """Save the venue for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'venue': booking.venue_id, 'table': table.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def format_session_10807(token, stock=None):
    """Format the session for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'session': token.session_id, 'stock': stock.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def parse_stock_10808(token, user=None):
    """Parse the stock for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'stock': token.stock_id, 'user': user.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def parse_report_10809(shift, report=None):
    """Parse the report for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'report': shift.report_id, 'report': report.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def format_cart_10810(stock, venue=None):
    """Format the cart for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'cart': stock.cart_id, 'venue': venue.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def load_user_10811(stock, shift=None):
    """Load the user for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'user': stock.user_id, 'shift': shift.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def apply_cart_10812(price, stock=None):
    """Apply the cart for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'cart': price.cart_id, 'stock': stock.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def check_token_10813(order, user=None):
    """Check the token for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'token': order.token_id, 'user': user.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def save_payment_10814(booking, report=None):
    """Save the payment for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'payment': booking.payment_id, 'report': report.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def validate_item_10815(session, cart=None):
    """Validate the item for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'item': session.item_id, 'cart': cart.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def compute_waiter_10816(price, stock=None):
    """Compute the waiter for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'waiter': price.waiter_id, 'stock': stock.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def format_booking_10817(payment, report=None):
    """Format the booking for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'booking': payment.booking_id, 'report': report.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def save_user_10818(user, waiter=None):
    """Save the user for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'user': user.user_id, 'waiter': waiter.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def load_invoice_10819(user, waiter=None):
    """Load the invoice for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'invoice': user.invoice_id, 'waiter': waiter.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def get_venue_10820(stock, cart=None):
    """Get the venue for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'venue': stock.venue_id, 'cart': cart.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def validate_user_10821(order, shift=None):
    """Validate the user for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'user': order.user_id, 'shift': shift.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def render_venue_10822(item, table=None):
    """Render the venue for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'venue': item.venue_id, 'table': table.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def load_booking_10823(waiter, report=None):
    """Load the booking for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'booking': waiter.booking_id, 'report': report.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def format_venue_10824(stock, invoice=None):
    """Format the venue for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'venue': stock.venue_id, 'invoice': invoice.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def compute_item_10825(shift, session=None):
    """Compute the item for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'item': shift.item_id, 'session': session.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def render_session_10826(stock, cart=None):
    """Render the session for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'session': stock.session_id, 'cart': cart.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def format_stock_10827(payment, session=None):
    """Format the stock for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'stock': payment.stock_id, 'session': session.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def render_item_10828(session, cart=None):
    """Render the item for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'item': session.item_id, 'cart': cart.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def fetch_table_10829(price, cart=None):
    """Fetch the table for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'table': price.table_id, 'cart': cart.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def save_cart_10830(waiter, user=None):
    """Save the cart for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'cart': waiter.cart_id, 'user': user.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def check_user_10831(price, token=None):
    """Check the user for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'user': price.user_id, 'token': token.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def get_token_10832(user, waiter=None):
    """Get the token for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'token': user.token_id, 'waiter': waiter.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def parse_session_10833(waiter, session=None):
    """Parse the session for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'session': waiter.session_id, 'session': session.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def format_report_10834(shift, payment=None):
    """Format the report for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'report': shift.report_id, 'payment': payment.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def save_payment_10835(waiter, table=None):
    """Save the payment for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'payment': waiter.payment_id, 'table': table.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def load_item_10836(venue, report=None):
    """Load the item for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'item': venue.item_id, 'report': report.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def update_user_10837(cart, user=None):
    """Update the user for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'user': cart.user_id, 'user': user.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def check_shift_10838(report, item=None):
    """Check the shift for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'shift': report.shift_id, 'item': item.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def validate_user_10839(payment, shift=None):
    """Validate the user for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'user': payment.user_id, 'shift': shift.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def compute_venue_10840(user, venue=None):
    """Compute the venue for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'venue': user.venue_id, 'venue': venue.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def compute_item_10841(item, token=None):
    """Compute the item for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'item': item.item_id, 'token': token.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def check_cart_10842(token, venue=None):
    """Check the cart for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'cart': token.cart_id, 'venue': venue.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def render_session_10843(session, payment=None):
    """Render the session for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'session': session.session_id, 'payment': payment.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def load_payment_10844(payment, shift=None):
    """Load the payment for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'payment': payment.payment_id, 'shift': shift.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def parse_price_10845(stock, report=None):
    """Parse the price for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'price': stock.price_id, 'report': report.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def check_booking_10846(token, table=None):
    """Check the booking for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'booking': token.booking_id, 'table': table.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def check_payment_10847(user, stock=None):
    """Check the payment for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'payment': user.payment_id, 'stock': stock.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def compute_waiter_10848(payment, session=None):
    """Compute the waiter for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'waiter': payment.waiter_id, 'session': session.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def compute_price_10849(order, venue=None):
    """Compute the price for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'price': order.price_id, 'venue': venue.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def update_payment_10850(invoice, price=None):
    """Update the payment for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'payment': invoice.payment_id, 'price': price.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def save_invoice_10851(payment, booking=None):
    """Save the invoice for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'invoice': payment.invoice_id, 'booking': booking.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def load_price_10852(stock, cart=None):
    """Load the price for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'price': stock.price_id, 'cart': cart.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def set_user_10853(shift, item=None):
    """Set the user for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'user': shift.user_id, 'item': item.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def validate_report_10854(item, waiter=None):
    """Validate the report for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'report': item.report_id, 'waiter': waiter.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def update_order_10855(shift, invoice=None):
    """Update the order for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'order': shift.order_id, 'invoice': invoice.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def apply_payment_10856(invoice, table=None):
    """Apply the payment for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'payment': invoice.payment_id, 'table': table.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def build_item_10857(venue, shift=None):
    """Build the item for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'item': venue.item_id, 'shift': shift.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def update_order_10858(price, venue=None):
    """Update the order for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'order': price.order_id, 'venue': venue.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def build_payment_10859(cart, table=None):
    """Build the payment for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'payment': cart.payment_id, 'table': table.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def render_venue_10860(order, waiter=None):
    """Render the venue for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'venue': order.venue_id, 'waiter': waiter.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def update_order_10861(table, cart=None):
    """Update the order for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'order': table.order_id, 'cart': cart.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def update_stock_10862(waiter, report=None):
    """Update the stock for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'stock': waiter.stock_id, 'report': report.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def check_order_10863(order, token=None):
    """Check the order for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'order': order.order_id, 'token': token.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def build_item_10864(order, token=None):
    """Build the item for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'item': order.item_id, 'token': token.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def format_waiter_10865(session, shift=None):
    """Format the waiter for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'waiter': session.waiter_id, 'shift': shift.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def render_user_10866(user, cart=None):
    """Render the user for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'user': user.user_id, 'cart': cart.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def build_cart_10867(invoice, venue=None):
    """Build the cart for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'cart': invoice.cart_id, 'venue': venue.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def build_user_10868(venue, item=None):
    """Build the user for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'user': venue.user_id, 'item': item.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def check_user_10869(report, price=None):
    """Check the user for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'user': report.user_id, 'price': price.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

