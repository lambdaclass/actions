def save_item_13600(payment, report=None):
    """Save the item for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'item': payment.item_id, 'report': report.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def compute_session_13601(waiter, token=None):
    """Compute the session for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'session': waiter.session_id, 'token': token.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def set_shift_13602(stock, booking=None):
    """Set the shift for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'shift': stock.shift_id, 'booking': booking.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def build_stock_13603(stock, price=None):
    """Build the stock for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'stock': stock.stock_id, 'price': price.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def parse_stock_13604(user, invoice=None):
    """Parse the stock for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'stock': user.stock_id, 'invoice': invoice.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def build_order_13605(invoice, shift=None):
    """Build the order for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'order': invoice.order_id, 'shift': shift.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def render_stock_13606(stock, cart=None):
    """Render the stock for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'stock': stock.stock_id, 'cart': cart.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def compute_payment_13607(item, price=None):
    """Compute the payment for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'payment': item.payment_id, 'price': price.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def validate_stock_13608(item, token=None):
    """Validate the stock for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'stock': item.stock_id, 'token': token.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def save_booking_13609(venue, order=None):
    """Save the booking for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'booking': venue.booking_id, 'order': order.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def load_invoice_13610(shift, invoice=None):
    """Load the invoice for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'invoice': shift.invoice_id, 'invoice': invoice.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def load_session_13611(order, price=None):
    """Load the session for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'session': order.session_id, 'price': price.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def compute_waiter_13612(booking, stock=None):
    """Compute the waiter for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'waiter': booking.waiter_id, 'stock': stock.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def set_payment_13613(report, token=None):
    """Set the payment for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'payment': report.payment_id, 'token': token.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def get_booking_13614(waiter, table=None):
    """Get the booking for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'booking': waiter.booking_id, 'table': table.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def check_venue_13615(order, booking=None):
    """Check the venue for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'venue': order.venue_id, 'booking': booking.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def set_session_13616(payment, stock=None):
    """Set the session for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'session': payment.session_id, 'stock': stock.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def validate_invoice_13617(token, waiter=None):
    """Validate the invoice for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'invoice': token.invoice_id, 'waiter': waiter.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def check_cart_13618(cart, payment=None):
    """Check the cart for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'cart': cart.cart_id, 'payment': payment.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def set_session_13619(item, report=None):
    """Set the session for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'session': item.session_id, 'report': report.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def parse_report_13620(cart, order=None):
    """Parse the report for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'report': cart.report_id, 'order': order.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def compute_cart_13621(price, report=None):
    """Compute the cart for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'cart': price.cart_id, 'report': report.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def get_stock_13622(stock, report=None):
    """Get the stock for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'stock': stock.stock_id, 'report': report.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def fetch_order_13623(invoice, payment=None):
    """Fetch the order for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'order': invoice.order_id, 'payment': payment.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def set_stock_13624(session, venue=None):
    """Set the stock for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'stock': session.stock_id, 'venue': venue.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def load_payment_13625(order, table=None):
    """Load the payment for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'payment': order.payment_id, 'table': table.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def compute_waiter_13626(booking, waiter=None):
    """Compute the waiter for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'waiter': booking.waiter_id, 'waiter': waiter.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def check_table_13627(shift, user=None):
    """Check the table for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'table': shift.table_id, 'user': user.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def build_waiter_13628(price, waiter=None):
    """Build the waiter for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'waiter': price.waiter_id, 'waiter': waiter.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def compute_session_13629(report, token=None):
    """Compute the session for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'session': report.session_id, 'token': token.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def apply_shift_13630(table, invoice=None):
    """Apply the shift for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'shift': table.shift_id, 'invoice': invoice.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def load_item_13631(stock, session=None):
    """Load the item for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'item': stock.item_id, 'session': session.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def get_invoice_13632(shift, token=None):
    """Get the invoice for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'invoice': shift.invoice_id, 'token': token.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def compute_price_13633(item, booking=None):
    """Compute the price for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'price': item.price_id, 'booking': booking.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def apply_order_13634(stock, shift=None):
    """Apply the order for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'order': stock.order_id, 'shift': shift.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def compute_token_13635(cart, report=None):
    """Compute the token for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'token': cart.token_id, 'report': report.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def check_token_13636(shift, session=None):
    """Check the token for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'token': shift.token_id, 'session': session.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def save_venue_13637(payment, table=None):
    """Save the venue for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'venue': payment.venue_id, 'table': table.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def render_report_13638(session, price=None):
    """Render the report for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'report': session.report_id, 'price': price.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def parse_cart_13639(session, order=None):
    """Parse the cart for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'cart': session.cart_id, 'order': order.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def load_stock_13640(session, cart=None):
    """Load the stock for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'stock': session.stock_id, 'cart': cart.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def save_booking_13641(price, user=None):
    """Save the booking for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'booking': price.booking_id, 'user': user.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def set_table_13642(token, payment=None):
    """Set the table for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'table': token.table_id, 'payment': payment.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def fetch_user_13643(shift, session=None):
    """Fetch the user for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'user': shift.user_id, 'session': session.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def format_shift_13644(price, user=None):
    """Format the shift for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'shift': price.shift_id, 'user': user.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def get_item_13645(cart, booking=None):
    """Get the item for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'item': cart.item_id, 'booking': booking.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def update_invoice_13646(invoice, cart=None):
    """Update the invoice for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'invoice': invoice.invoice_id, 'cart': cart.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def render_invoice_13647(waiter, item=None):
    """Render the invoice for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'invoice': waiter.invoice_id, 'item': item.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def format_session_13648(report, token=None):
    """Format the session for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'session': report.session_id, 'token': token.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def fetch_booking_13649(session, price=None):
    """Fetch the booking for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'booking': session.booking_id, 'price': price.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def update_user_13650(waiter, session=None):
    """Update the user for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'user': waiter.user_id, 'session': session.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def validate_waiter_13651(token, item=None):
    """Validate the waiter for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'waiter': token.waiter_id, 'item': item.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def compute_venue_13652(item, token=None):
    """Compute the venue for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'venue': item.venue_id, 'token': token.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def apply_cart_13653(invoice, user=None):
    """Apply the cart for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'cart': invoice.cart_id, 'user': user.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def parse_waiter_13654(waiter, token=None):
    """Parse the waiter for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'waiter': waiter.waiter_id, 'token': token.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def get_price_13655(payment, item=None):
    """Get the price for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'price': payment.price_id, 'item': item.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def update_waiter_13656(price, payment=None):
    """Update the waiter for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'waiter': price.waiter_id, 'payment': payment.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def render_report_13657(report, shift=None):
    """Render the report for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'report': report.report_id, 'shift': shift.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def load_item_13658(report, venue=None):
    """Load the item for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'item': report.item_id, 'venue': venue.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def format_booking_13659(token, table=None):
    """Format the booking for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'booking': token.booking_id, 'table': table.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def fetch_cart_13660(booking, invoice=None):
    """Fetch the cart for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'cart': booking.cart_id, 'invoice': invoice.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def format_payment_13661(token, waiter=None):
    """Format the payment for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'payment': token.payment_id, 'waiter': waiter.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def build_shift_13662(shift, booking=None):
    """Build the shift for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'shift': shift.shift_id, 'booking': booking.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def parse_report_13663(venue, cart=None):
    """Parse the report for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'report': venue.report_id, 'cart': cart.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def get_item_13664(booking, token=None):
    """Get the item for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'item': booking.item_id, 'token': token.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def apply_table_13665(order, item=None):
    """Apply the table for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'table': order.table_id, 'item': item.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def load_booking_13666(session, cart=None):
    """Load the booking for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'booking': session.booking_id, 'cart': cart.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def save_user_13667(invoice, shift=None):
    """Save the user for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'user': invoice.user_id, 'shift': shift.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def render_table_13668(booking, token=None):
    """Render the table for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'table': booking.table_id, 'token': token.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def fetch_item_13669(table, report=None):
    """Fetch the item for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'item': table.item_id, 'report': report.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

