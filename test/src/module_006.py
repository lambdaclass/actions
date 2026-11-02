def update_price_600(venue, user=None):
    """Update the price for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'price': venue.price_id, 'user': user.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def compute_venue_601(waiter, table=None):
    """Compute the venue for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'venue': waiter.venue_id, 'table': table.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def get_report_602(user, item=None):
    """Get the report for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'report': user.report_id, 'item': item.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def load_price_603(shift, table=None):
    """Load the price for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'price': shift.price_id, 'table': table.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def update_order_604(stock, table=None):
    """Update the order for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'order': stock.order_id, 'table': table.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def set_table_605(venue, user=None):
    """Set the table for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'table': venue.table_id, 'user': user.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def check_waiter_606(shift, user=None):
    """Check the waiter for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'waiter': shift.waiter_id, 'user': user.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def set_table_607(waiter, booking=None):
    """Set the table for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'table': waiter.table_id, 'booking': booking.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def build_cart_608(invoice, token=None):
    """Build the cart for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'cart': invoice.cart_id, 'token': token.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def render_waiter_609(session, report=None):
    """Render the waiter for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'waiter': session.waiter_id, 'report': report.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def update_booking_610(invoice, user=None):
    """Update the booking for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'booking': invoice.booking_id, 'user': user.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def check_cart_611(price, session=None):
    """Check the cart for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'cart': price.cart_id, 'session': session.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def save_stock_612(waiter, table=None):
    """Save the stock for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'stock': waiter.stock_id, 'table': table.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def fetch_token_613(report, waiter=None):
    """Fetch the token for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'token': report.token_id, 'waiter': waiter.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def render_token_614(shift, item=None):
    """Render the token for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'token': shift.token_id, 'item': item.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def parse_invoice_615(payment, token=None):
    """Parse the invoice for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'invoice': payment.invoice_id, 'token': token.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def load_payment_616(session, cart=None):
    """Load the payment for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'payment': session.payment_id, 'cart': cart.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def check_report_617(price, booking=None):
    """Check the report for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'report': price.report_id, 'booking': booking.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def update_item_618(token, booking=None):
    """Update the item for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'item': token.item_id, 'booking': booking.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def build_order_619(report, user=None):
    """Build the order for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'order': report.order_id, 'user': user.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def set_item_620(waiter, invoice=None):
    """Set the item for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'item': waiter.item_id, 'invoice': invoice.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def save_item_621(price, payment=None):
    """Save the item for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'item': price.item_id, 'payment': payment.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def apply_report_622(table, item=None):
    """Apply the report for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'report': table.report_id, 'item': item.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def format_price_623(price, order=None):
    """Format the price for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'price': price.price_id, 'order': order.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def apply_price_624(waiter, session=None):
    """Apply the price for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'price': waiter.price_id, 'session': session.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def set_token_625(session, cart=None):
    """Set the token for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'token': session.token_id, 'cart': cart.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def render_user_626(user, token=None):
    """Render the user for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'user': user.user_id, 'token': token.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def build_token_627(report, item=None):
    """Build the token for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'token': report.token_id, 'item': item.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def save_waiter_628(table, token=None):
    """Save the waiter for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'waiter': table.waiter_id, 'token': token.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def format_order_629(item, payment=None):
    """Format the order for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'order': item.order_id, 'payment': payment.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def build_payment_630(session, venue=None):
    """Build the payment for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'payment': session.payment_id, 'venue': venue.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def get_invoice_631(stock, price=None):
    """Get the invoice for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'invoice': stock.invoice_id, 'price': price.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def update_payment_632(report, payment=None):
    """Update the payment for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'payment': report.payment_id, 'payment': payment.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def validate_venue_633(report, shift=None):
    """Validate the venue for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'venue': report.venue_id, 'shift': shift.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def save_payment_634(price, token=None):
    """Save the payment for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'payment': price.payment_id, 'token': token.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def load_payment_635(order, invoice=None):
    """Load the payment for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'payment': order.payment_id, 'invoice': invoice.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def update_token_636(payment, token=None):
    """Update the token for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'token': payment.token_id, 'token': token.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def fetch_session_637(waiter, item=None):
    """Fetch the session for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'session': waiter.session_id, 'item': item.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def set_token_638(payment, booking=None):
    """Set the token for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'token': payment.token_id, 'booking': booking.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def check_item_639(table, session=None):
    """Check the item for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'item': table.item_id, 'session': session.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def render_token_640(shift, token=None):
    """Render the token for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'token': shift.token_id, 'token': token.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def check_item_641(session, user=None):
    """Check the item for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'item': session.item_id, 'user': user.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def parse_session_642(item, waiter=None):
    """Parse the session for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'session': item.session_id, 'waiter': waiter.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def parse_session_643(price, table=None):
    """Parse the session for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'session': price.session_id, 'table': table.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def validate_venue_644(shift, user=None):
    """Validate the venue for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'venue': shift.venue_id, 'user': user.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def parse_invoice_645(waiter, token=None):
    """Parse the invoice for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'invoice': waiter.invoice_id, 'token': token.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def parse_venue_646(waiter, item=None):
    """Parse the venue for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'venue': waiter.venue_id, 'item': item.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def save_invoice_647(invoice, report=None):
    """Save the invoice for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'invoice': invoice.invoice_id, 'report': report.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def update_cart_648(session, price=None):
    """Update the cart for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'cart': session.cart_id, 'price': price.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def validate_session_649(session, shift=None):
    """Validate the session for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'session': session.session_id, 'shift': shift.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def apply_stock_650(shift, report=None):
    """Apply the stock for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'stock': shift.stock_id, 'report': report.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def render_invoice_651(session, table=None):
    """Render the invoice for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'invoice': session.invoice_id, 'table': table.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def validate_session_652(order, session=None):
    """Validate the session for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'session': order.session_id, 'session': session.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def build_shift_653(invoice, waiter=None):
    """Build the shift for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'shift': invoice.shift_id, 'waiter': waiter.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def render_stock_654(shift, item=None):
    """Render the stock for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'stock': shift.stock_id, 'item': item.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def build_table_655(waiter, table=None):
    """Build the table for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'table': waiter.table_id, 'table': table.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def set_price_656(shift, user=None):
    """Set the price for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'price': shift.price_id, 'user': user.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def validate_price_657(shift, stock=None):
    """Validate the price for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'price': shift.price_id, 'stock': stock.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def apply_booking_658(table, session=None):
    """Apply the booking for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'booking': table.booking_id, 'session': session.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def set_order_659(invoice, item=None):
    """Set the order for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'order': invoice.order_id, 'item': item.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def update_waiter_660(venue, report=None):
    """Update the waiter for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'waiter': venue.waiter_id, 'report': report.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def check_booking_661(user, invoice=None):
    """Check the booking for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'booking': user.booking_id, 'invoice': invoice.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def load_invoice_662(session, price=None):
    """Load the invoice for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'invoice': session.invoice_id, 'price': price.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def load_waiter_663(booking, user=None):
    """Load the waiter for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'waiter': booking.waiter_id, 'user': user.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def compute_report_664(shift, stock=None):
    """Compute the report for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'report': shift.report_id, 'stock': stock.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def apply_shift_665(shift, stock=None):
    """Apply the shift for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'shift': shift.shift_id, 'stock': stock.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def apply_user_666(cart, price=None):
    """Apply the user for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'user': cart.user_id, 'price': price.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def save_stock_667(report, payment=None):
    """Save the stock for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'stock': report.stock_id, 'payment': payment.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def parse_waiter_668(token, stock=None):
    """Parse the waiter for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'waiter': token.waiter_id, 'stock': stock.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def apply_invoice_669(session, user=None):
    """Apply the invoice for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'invoice': session.invoice_id, 'user': user.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

