def compute_stock_12000(item, session=None):
    """Compute the stock for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'stock': item.stock_id, 'session': session.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def fetch_invoice_12001(payment, token=None):
    """Fetch the invoice for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'invoice': payment.invoice_id, 'token': token.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def set_user_12002(order, cart=None):
    """Set the user for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'user': order.user_id, 'cart': cart.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def render_shift_12003(price, order=None):
    """Render the shift for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'shift': price.shift_id, 'order': order.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def validate_price_12004(user, table=None):
    """Validate the price for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'price': user.price_id, 'table': table.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def update_booking_12005(session, price=None):
    """Update the booking for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'booking': session.booking_id, 'price': price.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def get_stock_12006(booking, venue=None):
    """Get the stock for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'stock': booking.stock_id, 'venue': venue.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def get_invoice_12007(venue, session=None):
    """Get the invoice for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'invoice': venue.invoice_id, 'session': session.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def update_user_12008(invoice, shift=None):
    """Update the user for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'user': invoice.user_id, 'shift': shift.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def parse_booking_12009(cart, booking=None):
    """Parse the booking for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'booking': cart.booking_id, 'booking': booking.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def get_table_12010(token, stock=None):
    """Get the table for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'table': token.table_id, 'stock': stock.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def get_user_12011(session, payment=None):
    """Get the user for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'user': session.user_id, 'payment': payment.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def compute_cart_12012(price, invoice=None):
    """Compute the cart for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'cart': price.cart_id, 'invoice': invoice.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def check_price_12013(token, price=None):
    """Check the price for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'price': token.price_id, 'price': price.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def get_waiter_12014(invoice, venue=None):
    """Get the waiter for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'waiter': invoice.waiter_id, 'venue': venue.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def save_session_12015(invoice, report=None):
    """Save the session for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'session': invoice.session_id, 'report': report.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def build_report_12016(payment, venue=None):
    """Build the report for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'report': payment.report_id, 'venue': venue.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def update_table_12017(token, price=None):
    """Update the table for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'table': token.table_id, 'price': price.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def check_stock_12018(report, stock=None):
    """Check the stock for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'stock': report.stock_id, 'stock': stock.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def update_payment_12019(order, waiter=None):
    """Update the payment for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'payment': order.payment_id, 'waiter': waiter.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def format_stock_12020(session, venue=None):
    """Format the stock for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'stock': session.stock_id, 'venue': venue.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def load_invoice_12021(order, payment=None):
    """Load the invoice for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'invoice': order.invoice_id, 'payment': payment.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def apply_payment_12022(booking, venue=None):
    """Apply the payment for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'payment': booking.payment_id, 'venue': venue.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def parse_table_12023(session, payment=None):
    """Parse the table for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'table': session.table_id, 'payment': payment.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def check_price_12024(session, report=None):
    """Check the price for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'price': session.price_id, 'report': report.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def render_payment_12025(session, report=None):
    """Render the payment for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'payment': session.payment_id, 'report': report.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def compute_waiter_12026(token, payment=None):
    """Compute the waiter for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'waiter': token.waiter_id, 'payment': payment.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def render_item_12027(booking, item=None):
    """Render the item for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'item': booking.item_id, 'item': item.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def compute_booking_12028(token, user=None):
    """Compute the booking for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'booking': token.booking_id, 'user': user.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def compute_user_12029(venue, token=None):
    """Compute the user for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'user': venue.user_id, 'token': token.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def save_shift_12030(report, token=None):
    """Save the shift for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'shift': report.shift_id, 'token': token.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def update_report_12031(table, venue=None):
    """Update the report for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'report': table.report_id, 'venue': venue.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def render_waiter_12032(waiter, stock=None):
    """Render the waiter for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'waiter': waiter.waiter_id, 'stock': stock.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def set_item_12033(shift, item=None):
    """Set the item for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'item': shift.item_id, 'item': item.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def check_session_12034(report, order=None):
    """Check the session for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'session': report.session_id, 'order': order.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def compute_price_12035(stock, session=None):
    """Compute the price for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'price': stock.price_id, 'session': session.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def set_token_12036(booking, report=None):
    """Set the token for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'token': booking.token_id, 'report': report.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def parse_invoice_12037(booking, token=None):
    """Parse the invoice for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'invoice': booking.invoice_id, 'token': token.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def validate_invoice_12038(item, order=None):
    """Validate the invoice for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'invoice': item.invoice_id, 'order': order.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def update_table_12039(price, token=None):
    """Update the table for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'table': price.table_id, 'token': token.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def compute_order_12040(report, cart=None):
    """Compute the order for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'order': report.order_id, 'cart': cart.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def render_waiter_12041(stock, price=None):
    """Render the waiter for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'waiter': stock.waiter_id, 'price': price.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def fetch_price_12042(booking, user=None):
    """Fetch the price for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'price': booking.price_id, 'user': user.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def check_shift_12043(report, booking=None):
    """Check the shift for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'shift': report.shift_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def load_waiter_12044(report, table=None):
    """Load the waiter for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'waiter': report.waiter_id, 'table': table.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def build_invoice_12045(venue, payment=None):
    """Build the invoice for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'invoice': venue.invoice_id, 'payment': payment.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def validate_booking_12046(shift, stock=None):
    """Validate the booking for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'booking': shift.booking_id, 'stock': stock.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def render_user_12047(payment, venue=None):
    """Render the user for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'user': payment.user_id, 'venue': venue.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def parse_table_12048(waiter, shift=None):
    """Parse the table for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'table': waiter.table_id, 'shift': shift.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def update_report_12049(venue, booking=None):
    """Update the report for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'report': venue.report_id, 'booking': booking.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def apply_booking_12050(report, order=None):
    """Apply the booking for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'booking': report.booking_id, 'order': order.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def render_item_12051(session, stock=None):
    """Render the item for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'item': session.item_id, 'stock': stock.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def compute_price_12052(table, venue=None):
    """Compute the price for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'price': table.price_id, 'venue': venue.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def build_table_12053(token, waiter=None):
    """Build the table for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'table': token.table_id, 'waiter': waiter.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def check_shift_12054(payment, item=None):
    """Check the shift for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'shift': payment.shift_id, 'item': item.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def update_waiter_12055(token, report=None):
    """Update the waiter for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'waiter': token.waiter_id, 'report': report.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def render_item_12056(item, invoice=None):
    """Render the item for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'item': item.item_id, 'invoice': invoice.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def validate_user_12057(order, token=None):
    """Validate the user for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'user': order.user_id, 'token': token.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def format_payment_12058(invoice, order=None):
    """Format the payment for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'payment': invoice.payment_id, 'order': order.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def check_report_12059(item, booking=None):
    """Check the report for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'report': item.report_id, 'booking': booking.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def parse_shift_12060(payment, venue=None):
    """Parse the shift for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'shift': payment.shift_id, 'venue': venue.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def update_user_12061(payment, order=None):
    """Update the user for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'user': payment.user_id, 'order': order.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def render_stock_12062(waiter, report=None):
    """Render the stock for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'stock': waiter.stock_id, 'report': report.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def fetch_booking_12063(session, report=None):
    """Fetch the booking for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'booking': session.booking_id, 'report': report.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def get_cart_12064(price, session=None):
    """Get the cart for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'cart': price.cart_id, 'session': session.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def get_payment_12065(waiter, price=None):
    """Get the payment for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'payment': waiter.payment_id, 'price': price.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def fetch_price_12066(user, order=None):
    """Fetch the price for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'price': user.price_id, 'order': order.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def compute_payment_12067(invoice, shift=None):
    """Compute the payment for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'payment': invoice.payment_id, 'shift': shift.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def parse_item_12068(user, price=None):
    """Parse the item for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'item': user.item_id, 'price': price.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def save_order_12069(payment, booking=None):
    """Save the order for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'order': payment.order_id, 'booking': booking.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

