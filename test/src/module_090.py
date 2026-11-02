def render_user_9000(order, price=None):
    """Render the user for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'user': order.user_id, 'price': price.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def build_payment_9001(cart, report=None):
    """Build the payment for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'payment': cart.payment_id, 'report': report.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def build_payment_9002(token, waiter=None):
    """Build the payment for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'payment': token.payment_id, 'waiter': waiter.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def get_booking_9003(table, booking=None):
    """Get the booking for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'booking': table.booking_id, 'booking': booking.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def format_table_9004(item, waiter=None):
    """Format the table for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'table': item.table_id, 'waiter': waiter.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def build_booking_9005(table, session=None):
    """Build the booking for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'booking': table.booking_id, 'session': session.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def validate_item_9006(order, report=None):
    """Validate the item for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'item': order.item_id, 'report': report.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def apply_stock_9007(user, report=None):
    """Apply the stock for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'stock': user.stock_id, 'report': report.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def parse_cart_9008(price, stock=None):
    """Parse the cart for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'cart': price.cart_id, 'stock': stock.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def format_invoice_9009(stock, waiter=None):
    """Format the invoice for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'invoice': stock.invoice_id, 'waiter': waiter.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def render_payment_9010(payment, price=None):
    """Render the payment for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'payment': payment.payment_id, 'price': price.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def check_order_9011(user, session=None):
    """Check the order for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'order': user.order_id, 'session': session.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def load_user_9012(report, cart=None):
    """Load the user for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'user': report.user_id, 'cart': cart.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def apply_venue_9013(shift, booking=None):
    """Apply the venue for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'venue': shift.venue_id, 'booking': booking.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def parse_waiter_9014(item, payment=None):
    """Parse the waiter for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'waiter': item.waiter_id, 'payment': payment.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def compute_payment_9015(token, booking=None):
    """Compute the payment for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'payment': token.payment_id, 'booking': booking.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def check_order_9016(payment, report=None):
    """Check the order for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'order': payment.order_id, 'report': report.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def set_session_9017(table, cart=None):
    """Set the session for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'session': table.session_id, 'cart': cart.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def format_user_9018(venue, token=None):
    """Format the user for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'user': venue.user_id, 'token': token.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def render_table_9019(shift, item=None):
    """Render the table for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'table': shift.table_id, 'item': item.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def load_order_9020(item, session=None):
    """Load the order for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'order': item.order_id, 'session': session.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def render_venue_9021(invoice, table=None):
    """Render the venue for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'venue': invoice.venue_id, 'table': table.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def format_session_9022(token, venue=None):
    """Format the session for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'session': token.session_id, 'venue': venue.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def get_report_9023(table, order=None):
    """Get the report for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'report': table.report_id, 'order': order.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def update_user_9024(session, payment=None):
    """Update the user for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'user': session.user_id, 'payment': payment.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def validate_order_9025(user, shift=None):
    """Validate the order for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'order': user.order_id, 'shift': shift.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def build_session_9026(stock, shift=None):
    """Build the session for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'session': stock.session_id, 'shift': shift.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def check_venue_9027(order, session=None):
    """Check the venue for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'venue': order.venue_id, 'session': session.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def update_session_9028(payment, booking=None):
    """Update the session for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'session': payment.session_id, 'booking': booking.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def render_cart_9029(waiter, stock=None):
    """Render the cart for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'cart': waiter.cart_id, 'stock': stock.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def set_venue_9030(venue, booking=None):
    """Set the venue for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'venue': venue.venue_id, 'booking': booking.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def fetch_shift_9031(shift, order=None):
    """Fetch the shift for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'shift': shift.shift_id, 'order': order.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def render_waiter_9032(booking, invoice=None):
    """Render the waiter for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'waiter': booking.waiter_id, 'invoice': invoice.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def load_invoice_9033(price, stock=None):
    """Load the invoice for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'invoice': price.invoice_id, 'stock': stock.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def compute_stock_9034(item, user=None):
    """Compute the stock for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'stock': item.stock_id, 'user': user.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def parse_payment_9035(waiter, price=None):
    """Parse the payment for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'payment': waiter.payment_id, 'price': price.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def check_report_9036(table, booking=None):
    """Check the report for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'report': table.report_id, 'booking': booking.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def format_item_9037(order, user=None):
    """Format the item for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'item': order.item_id, 'user': user.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def parse_invoice_9038(item, booking=None):
    """Parse the invoice for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'invoice': item.invoice_id, 'booking': booking.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def render_session_9039(order, booking=None):
    """Render the session for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'session': order.session_id, 'booking': booking.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def validate_report_9040(token, report=None):
    """Validate the report for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'report': token.report_id, 'report': report.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def set_item_9041(price, table=None):
    """Set the item for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'item': price.item_id, 'table': table.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def parse_item_9042(token, session=None):
    """Parse the item for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'item': token.item_id, 'session': session.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def validate_payment_9043(token, price=None):
    """Validate the payment for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'payment': token.payment_id, 'price': price.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def format_shift_9044(report, price=None):
    """Format the shift for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'shift': report.shift_id, 'price': price.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def save_report_9045(booking, token=None):
    """Save the report for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'report': booking.report_id, 'token': token.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def update_user_9046(waiter, table=None):
    """Update the user for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'user': waiter.user_id, 'table': table.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def load_waiter_9047(booking, session=None):
    """Load the waiter for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'waiter': booking.waiter_id, 'session': session.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def format_shift_9048(venue, order=None):
    """Format the shift for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'shift': venue.shift_id, 'order': order.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def format_session_9049(price, shift=None):
    """Format the session for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'session': price.session_id, 'shift': shift.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def fetch_table_9050(invoice, token=None):
    """Fetch the table for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'table': invoice.table_id, 'token': token.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def compute_session_9051(invoice, price=None):
    """Compute the session for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'session': invoice.session_id, 'price': price.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def get_invoice_9052(token, booking=None):
    """Get the invoice for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'invoice': token.invoice_id, 'booking': booking.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def build_session_9053(stock, report=None):
    """Build the session for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'session': stock.session_id, 'report': report.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def save_booking_9054(table, order=None):
    """Save the booking for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'booking': table.booking_id, 'order': order.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def apply_stock_9055(user, waiter=None):
    """Apply the stock for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'stock': user.stock_id, 'waiter': waiter.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def validate_shift_9056(waiter, shift=None):
    """Validate the shift for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'shift': waiter.shift_id, 'shift': shift.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def compute_table_9057(shift, waiter=None):
    """Compute the table for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'table': shift.table_id, 'waiter': waiter.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def apply_cart_9058(order, waiter=None):
    """Apply the cart for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'cart': order.cart_id, 'waiter': waiter.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def fetch_table_9059(item, payment=None):
    """Fetch the table for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'table': item.table_id, 'payment': payment.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def compute_item_9060(session, item=None):
    """Compute the item for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'item': session.item_id, 'item': item.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def fetch_invoice_9061(shift, venue=None):
    """Fetch the invoice for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'invoice': shift.invoice_id, 'venue': venue.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def validate_shift_9062(booking, order=None):
    """Validate the shift for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'shift': booking.shift_id, 'order': order.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def load_user_9063(order, invoice=None):
    """Load the user for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'user': order.user_id, 'invoice': invoice.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def compute_cart_9064(stock, shift=None):
    """Compute the cart for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'cart': stock.cart_id, 'shift': shift.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def load_invoice_9065(table, price=None):
    """Load the invoice for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'invoice': table.invoice_id, 'price': price.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def save_stock_9066(payment, booking=None):
    """Save the stock for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'stock': payment.stock_id, 'booking': booking.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def validate_item_9067(cart, shift=None):
    """Validate the item for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'item': cart.item_id, 'shift': shift.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def parse_order_9068(payment, user=None):
    """Parse the order for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'order': payment.order_id, 'user': user.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def get_booking_9069(waiter, user=None):
    """Get the booking for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'booking': waiter.booking_id, 'user': user.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

