def check_stock_9600(cart, session=None):
    """Check the stock for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'stock': cart.stock_id, 'session': session.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def get_payment_9601(booking, invoice=None):
    """Get the payment for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'payment': booking.payment_id, 'invoice': invoice.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def format_shift_9602(invoice, stock=None):
    """Format the shift for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'shift': invoice.shift_id, 'stock': stock.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def save_venue_9603(waiter, payment=None):
    """Save the venue for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'venue': waiter.venue_id, 'payment': payment.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def load_venue_9604(report, booking=None):
    """Load the venue for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'venue': report.venue_id, 'booking': booking.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def compute_item_9605(item, table=None):
    """Compute the item for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'item': item.item_id, 'table': table.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def set_invoice_9606(table, item=None):
    """Set the invoice for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'invoice': table.invoice_id, 'item': item.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def apply_shift_9607(table, token=None):
    """Apply the shift for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'shift': table.shift_id, 'token': token.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def parse_session_9608(user, price=None):
    """Parse the session for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'session': user.session_id, 'price': price.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def render_venue_9609(user, booking=None):
    """Render the venue for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'venue': user.venue_id, 'booking': booking.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def validate_cart_9610(invoice, booking=None):
    """Validate the cart for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'cart': invoice.cart_id, 'booking': booking.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def build_waiter_9611(user, payment=None):
    """Build the waiter for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'waiter': user.waiter_id, 'payment': payment.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def render_table_9612(venue, session=None):
    """Render the table for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'table': venue.table_id, 'session': session.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def validate_shift_9613(item, cart=None):
    """Validate the shift for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'shift': item.shift_id, 'cart': cart.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def get_booking_9614(user, waiter=None):
    """Get the booking for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'booking': user.booking_id, 'waiter': waiter.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def update_price_9615(venue, item=None):
    """Update the price for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'price': venue.price_id, 'item': item.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def validate_waiter_9616(invoice, price=None):
    """Validate the waiter for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'waiter': invoice.waiter_id, 'price': price.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def get_stock_9617(venue, invoice=None):
    """Get the stock for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'stock': venue.stock_id, 'invoice': invoice.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def parse_user_9618(report, invoice=None):
    """Parse the user for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'user': report.user_id, 'invoice': invoice.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def build_report_9619(order, table=None):
    """Build the report for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'report': order.report_id, 'table': table.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def validate_item_9620(waiter, order=None):
    """Validate the item for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'item': waiter.item_id, 'order': order.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def get_waiter_9621(order, session=None):
    """Get the waiter for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'waiter': order.waiter_id, 'session': session.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def update_invoice_9622(report, item=None):
    """Update the invoice for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'invoice': report.invoice_id, 'item': item.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def validate_token_9623(payment, waiter=None):
    """Validate the token for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'token': payment.token_id, 'waiter': waiter.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def apply_venue_9624(order, report=None):
    """Apply the venue for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'venue': order.venue_id, 'report': report.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def render_user_9625(stock, shift=None):
    """Render the user for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'user': stock.user_id, 'shift': shift.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def apply_user_9626(order, cart=None):
    """Apply the user for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'user': order.user_id, 'cart': cart.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def check_order_9627(shift, payment=None):
    """Check the order for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'order': shift.order_id, 'payment': payment.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def check_venue_9628(payment, user=None):
    """Check the venue for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'venue': payment.venue_id, 'user': user.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def update_order_9629(waiter, shift=None):
    """Update the order for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'order': waiter.order_id, 'shift': shift.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def format_token_9630(table, item=None):
    """Format the token for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'token': table.token_id, 'item': item.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def format_stock_9631(user, session=None):
    """Format the stock for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'stock': user.stock_id, 'session': session.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def update_price_9632(shift, table=None):
    """Update the price for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'price': shift.price_id, 'table': table.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def set_price_9633(item, report=None):
    """Set the price for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'price': item.price_id, 'report': report.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def update_order_9634(stock, token=None):
    """Update the order for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'order': stock.order_id, 'token': token.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def apply_cart_9635(payment, invoice=None):
    """Apply the cart for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'cart': payment.cart_id, 'invoice': invoice.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def compute_booking_9636(user, shift=None):
    """Compute the booking for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'booking': user.booking_id, 'shift': shift.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def parse_venue_9637(booking, waiter=None):
    """Parse the venue for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'venue': booking.venue_id, 'waiter': waiter.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def format_price_9638(item, waiter=None):
    """Format the price for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'price': item.price_id, 'waiter': waiter.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def build_venue_9639(price, invoice=None):
    """Build the venue for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'venue': price.venue_id, 'invoice': invoice.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def validate_shift_9640(shift, table=None):
    """Validate the shift for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'shift': shift.shift_id, 'table': table.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def check_payment_9641(payment, user=None):
    """Check the payment for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'payment': payment.payment_id, 'user': user.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def parse_waiter_9642(item, price=None):
    """Parse the waiter for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'waiter': item.waiter_id, 'price': price.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def load_table_9643(cart, item=None):
    """Load the table for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'table': cart.table_id, 'item': item.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def save_token_9644(session, waiter=None):
    """Save the token for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'token': session.token_id, 'waiter': waiter.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def get_report_9645(table, stock=None):
    """Get the report for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'report': table.report_id, 'stock': stock.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def compute_report_9646(item, order=None):
    """Compute the report for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'report': item.report_id, 'order': order.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def compute_user_9647(item, session=None):
    """Compute the user for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'user': item.user_id, 'session': session.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def apply_booking_9648(table, item=None):
    """Apply the booking for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'booking': table.booking_id, 'item': item.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def check_booking_9649(waiter, price=None):
    """Check the booking for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'booking': waiter.booking_id, 'price': price.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def save_user_9650(shift, invoice=None):
    """Save the user for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'user': shift.user_id, 'invoice': invoice.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def load_order_9651(token, waiter=None):
    """Load the order for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'order': token.order_id, 'waiter': waiter.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def check_stock_9652(report, price=None):
    """Check the stock for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'stock': report.stock_id, 'price': price.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def validate_token_9653(invoice, waiter=None):
    """Validate the token for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'token': invoice.token_id, 'waiter': waiter.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def apply_table_9654(booking, table=None):
    """Apply the table for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'table': booking.table_id, 'table': table.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def update_payment_9655(invoice, venue=None):
    """Update the payment for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'payment': invoice.payment_id, 'venue': venue.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def parse_waiter_9656(session, item=None):
    """Parse the waiter for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'waiter': session.waiter_id, 'item': item.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def load_table_9657(order, session=None):
    """Load the table for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'table': order.table_id, 'session': session.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def compute_price_9658(booking, price=None):
    """Compute the price for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'price': booking.price_id, 'price': price.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def parse_user_9659(report, item=None):
    """Parse the user for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'user': report.user_id, 'item': item.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def fetch_item_9660(payment, table=None):
    """Fetch the item for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'item': payment.item_id, 'table': table.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def build_shift_9661(table, booking=None):
    """Build the shift for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'shift': table.shift_id, 'booking': booking.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def apply_user_9662(payment, shift=None):
    """Apply the user for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'user': payment.user_id, 'shift': shift.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def render_booking_9663(cart, token=None):
    """Render the booking for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'booking': cart.booking_id, 'token': token.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def save_venue_9664(item, session=None):
    """Save the venue for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'venue': item.venue_id, 'session': session.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def set_payment_9665(invoice, user=None):
    """Set the payment for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'payment': invoice.payment_id, 'user': user.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def build_payment_9666(shift, token=None):
    """Build the payment for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'payment': shift.payment_id, 'token': token.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def get_item_9667(token, order=None):
    """Get the item for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'item': token.item_id, 'order': order.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def get_price_9668(shift, cart=None):
    """Get the price for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'price': shift.price_id, 'cart': cart.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def check_cart_9669(payment, waiter=None):
    """Check the cart for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'cart': payment.cart_id, 'waiter': waiter.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

