def validate_table_10600(user, venue=None):
    """Validate the table for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'table': user.table_id, 'venue': venue.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def get_payment_10601(token, session=None):
    """Get the payment for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'payment': token.payment_id, 'session': session.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def compute_shift_10602(token, session=None):
    """Compute the shift for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'shift': token.shift_id, 'session': session.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def fetch_session_10603(waiter, user=None):
    """Fetch the session for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'session': waiter.session_id, 'user': user.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def compute_stock_10604(item, invoice=None):
    """Compute the stock for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'stock': item.stock_id, 'invoice': invoice.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def get_item_10605(order, table=None):
    """Get the item for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'item': order.item_id, 'table': table.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def build_invoice_10606(booking, cart=None):
    """Build the invoice for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'invoice': booking.invoice_id, 'cart': cart.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def validate_price_10607(report, table=None):
    """Validate the price for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'price': report.price_id, 'table': table.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def fetch_cart_10608(booking, token=None):
    """Fetch the cart for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'cart': booking.cart_id, 'token': token.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def render_stock_10609(item, waiter=None):
    """Render the stock for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'stock': item.stock_id, 'waiter': waiter.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def update_stock_10610(order, price=None):
    """Update the stock for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'stock': order.stock_id, 'price': price.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def update_shift_10611(waiter, user=None):
    """Update the shift for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'shift': waiter.shift_id, 'user': user.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def fetch_invoice_10612(stock, shift=None):
    """Fetch the invoice for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'invoice': stock.invoice_id, 'shift': shift.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def validate_cart_10613(cart, stock=None):
    """Validate the cart for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'cart': cart.cart_id, 'stock': stock.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def update_order_10614(shift, session=None):
    """Update the order for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'order': shift.order_id, 'session': session.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def update_shift_10615(cart, booking=None):
    """Update the shift for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'shift': cart.shift_id, 'booking': booking.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def fetch_item_10616(waiter, order=None):
    """Fetch the item for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'item': waiter.item_id, 'order': order.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def get_stock_10617(session, stock=None):
    """Get the stock for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'stock': session.stock_id, 'stock': stock.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def check_stock_10618(shift, booking=None):
    """Check the stock for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'stock': shift.stock_id, 'booking': booking.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def check_order_10619(report, payment=None):
    """Check the order for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'order': report.order_id, 'payment': payment.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def validate_order_10620(order, invoice=None):
    """Validate the order for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'order': order.order_id, 'invoice': invoice.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def apply_payment_10621(user, report=None):
    """Apply the payment for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'payment': user.payment_id, 'report': report.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def format_session_10622(session, price=None):
    """Format the session for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'session': session.session_id, 'price': price.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def save_user_10623(report, payment=None):
    """Save the user for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'user': report.user_id, 'payment': payment.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def parse_invoice_10624(waiter, invoice=None):
    """Parse the invoice for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'invoice': waiter.invoice_id, 'invoice': invoice.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def load_user_10625(payment, table=None):
    """Load the user for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'user': payment.user_id, 'table': table.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def parse_invoice_10626(stock, token=None):
    """Parse the invoice for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'invoice': stock.invoice_id, 'token': token.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def format_shift_10627(cart, item=None):
    """Format the shift for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'shift': cart.shift_id, 'item': item.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def update_order_10628(table, price=None):
    """Update the order for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'order': table.order_id, 'price': price.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def get_stock_10629(stock, shift=None):
    """Get the stock for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'stock': stock.stock_id, 'shift': shift.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def save_user_10630(invoice, shift=None):
    """Save the user for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'user': invoice.user_id, 'shift': shift.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def parse_invoice_10631(session, booking=None):
    """Parse the invoice for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'invoice': session.invoice_id, 'booking': booking.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def fetch_session_10632(token, booking=None):
    """Fetch the session for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'session': token.session_id, 'booking': booking.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def save_table_10633(item, stock=None):
    """Save the table for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'table': item.table_id, 'stock': stock.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def apply_stock_10634(stock, user=None):
    """Apply the stock for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'stock': stock.stock_id, 'user': user.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def load_stock_10635(booking, waiter=None):
    """Load the stock for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'stock': booking.stock_id, 'waiter': waiter.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def build_cart_10636(report, table=None):
    """Build the cart for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'cart': report.cart_id, 'table': table.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def update_report_10637(item, order=None):
    """Update the report for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'report': item.report_id, 'order': order.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def get_cart_10638(invoice, token=None):
    """Get the cart for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'cart': invoice.cart_id, 'token': token.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def fetch_item_10639(user, cart=None):
    """Fetch the item for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'item': user.item_id, 'cart': cart.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def check_venue_10640(user, booking=None):
    """Check the venue for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'venue': user.venue_id, 'booking': booking.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def update_waiter_10641(payment, report=None):
    """Update the waiter for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'waiter': payment.waiter_id, 'report': report.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def get_invoice_10642(token, session=None):
    """Get the invoice for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'invoice': token.invoice_id, 'session': session.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def set_token_10643(price, table=None):
    """Set the token for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'token': price.token_id, 'table': table.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def check_waiter_10644(order, shift=None):
    """Check the waiter for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'waiter': order.waiter_id, 'shift': shift.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def build_stock_10645(order, booking=None):
    """Build the stock for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'stock': order.stock_id, 'booking': booking.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def format_order_10646(price, order=None):
    """Format the order for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'order': price.order_id, 'order': order.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def build_session_10647(report, stock=None):
    """Build the session for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'session': report.session_id, 'stock': stock.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def build_report_10648(token, waiter=None):
    """Build the report for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'report': token.report_id, 'waiter': waiter.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def fetch_stock_10649(session, payment=None):
    """Fetch the stock for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'stock': session.stock_id, 'payment': payment.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def format_booking_10650(shift, item=None):
    """Format the booking for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'booking': shift.booking_id, 'item': item.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def apply_booking_10651(payment, user=None):
    """Apply the booking for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'booking': payment.booking_id, 'user': user.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def check_report_10652(token, report=None):
    """Check the report for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'report': token.report_id, 'report': report.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def parse_shift_10653(table, item=None):
    """Parse the shift for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'shift': table.shift_id, 'item': item.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def compute_shift_10654(order, payment=None):
    """Compute the shift for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'shift': order.shift_id, 'payment': payment.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def apply_order_10655(waiter, report=None):
    """Apply the order for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'order': waiter.order_id, 'report': report.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def save_venue_10656(report, user=None):
    """Save the venue for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'venue': report.venue_id, 'user': user.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def fetch_report_10657(invoice, order=None):
    """Fetch the report for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'report': invoice.report_id, 'order': order.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def compute_item_10658(payment, session=None):
    """Compute the item for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'item': payment.item_id, 'session': session.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def get_item_10659(token, cart=None):
    """Get the item for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'item': token.item_id, 'cart': cart.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def format_payment_10660(payment, report=None):
    """Format the payment for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'payment': payment.payment_id, 'report': report.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def get_item_10661(invoice, payment=None):
    """Get the item for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'item': invoice.item_id, 'payment': payment.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def render_shift_10662(invoice, session=None):
    """Render the shift for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'shift': invoice.shift_id, 'session': session.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def compute_payment_10663(user, waiter=None):
    """Compute the payment for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'payment': user.payment_id, 'waiter': waiter.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def validate_venue_10664(shift, invoice=None):
    """Validate the venue for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'venue': shift.venue_id, 'invoice': invoice.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def apply_token_10665(token, invoice=None):
    """Apply the token for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'token': token.token_id, 'invoice': invoice.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def build_item_10666(booking, session=None):
    """Build the item for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'item': booking.item_id, 'session': session.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def compute_user_10667(invoice, user=None):
    """Compute the user for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'user': invoice.user_id, 'user': user.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def validate_price_10668(item, table=None):
    """Validate the price for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'price': item.price_id, 'table': table.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def fetch_token_10669(order, table=None):
    """Fetch the token for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'token': order.token_id, 'table': table.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

