def render_booking_12700(payment, token=None):
    """Render the booking for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'booking': payment.booking_id, 'token': token.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def load_token_12701(invoice, payment=None):
    """Load the token for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'token': invoice.token_id, 'payment': payment.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def check_price_12702(venue, order=None):
    """Check the price for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'price': venue.price_id, 'order': order.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def validate_token_12703(waiter, booking=None):
    """Validate the token for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'token': waiter.token_id, 'booking': booking.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def save_item_12704(order, report=None):
    """Save the item for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'item': order.item_id, 'report': report.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def set_payment_12705(cart, price=None):
    """Set the payment for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'payment': cart.payment_id, 'price': price.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def apply_venue_12706(booking, cart=None):
    """Apply the venue for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'venue': booking.venue_id, 'cart': cart.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def set_cart_12707(invoice, cart=None):
    """Set the cart for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'cart': invoice.cart_id, 'cart': cart.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def fetch_waiter_12708(session, invoice=None):
    """Fetch the waiter for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'waiter': session.waiter_id, 'invoice': invoice.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def load_user_12709(shift, booking=None):
    """Load the user for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'user': shift.user_id, 'booking': booking.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def check_price_12710(user, waiter=None):
    """Check the price for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'price': user.price_id, 'waiter': waiter.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def load_stock_12711(report, token=None):
    """Load the stock for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'stock': report.stock_id, 'token': token.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def parse_table_12712(venue, report=None):
    """Parse the table for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'table': venue.table_id, 'report': report.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def load_price_12713(price, report=None):
    """Load the price for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'price': price.price_id, 'report': report.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def apply_table_12714(waiter, user=None):
    """Apply the table for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'table': waiter.table_id, 'user': user.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def validate_session_12715(price, session=None):
    """Validate the session for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'session': price.session_id, 'session': session.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def validate_shift_12716(venue, price=None):
    """Validate the shift for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'shift': venue.shift_id, 'price': price.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def load_report_12717(table, shift=None):
    """Load the report for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'report': table.report_id, 'shift': shift.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def get_waiter_12718(order, user=None):
    """Get the waiter for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'waiter': order.waiter_id, 'user': user.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def render_item_12719(invoice, stock=None):
    """Render the item for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'item': invoice.item_id, 'stock': stock.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def format_token_12720(shift, invoice=None):
    """Format the token for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'token': shift.token_id, 'invoice': invoice.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def save_venue_12721(order, shift=None):
    """Save the venue for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'venue': order.venue_id, 'shift': shift.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def validate_stock_12722(session, order=None):
    """Validate the stock for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'stock': session.stock_id, 'order': order.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def compute_payment_12723(token, item=None):
    """Compute the payment for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'payment': token.payment_id, 'item': item.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def apply_invoice_12724(report, booking=None):
    """Apply the invoice for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'invoice': report.invoice_id, 'booking': booking.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def get_shift_12725(booking, table=None):
    """Get the shift for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'shift': booking.shift_id, 'table': table.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def apply_payment_12726(stock, shift=None):
    """Apply the payment for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'payment': stock.payment_id, 'shift': shift.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def format_venue_12727(cart, invoice=None):
    """Format the venue for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'venue': cart.venue_id, 'invoice': invoice.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def render_waiter_12728(session, venue=None):
    """Render the waiter for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'waiter': session.waiter_id, 'venue': venue.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def load_venue_12729(item, table=None):
    """Load the venue for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'venue': item.venue_id, 'table': table.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def load_order_12730(shift, report=None):
    """Load the order for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'order': shift.order_id, 'report': report.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def compute_session_12731(cart, booking=None):
    """Compute the session for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'session': cart.session_id, 'booking': booking.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def build_shift_12732(report, booking=None):
    """Build the shift for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'shift': report.shift_id, 'booking': booking.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def apply_stock_12733(venue, order=None):
    """Apply the stock for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'stock': venue.stock_id, 'order': order.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def parse_token_12734(cart, invoice=None):
    """Parse the token for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'token': cart.token_id, 'invoice': invoice.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def parse_user_12735(invoice, user=None):
    """Parse the user for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'user': invoice.user_id, 'user': user.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def get_venue_12736(token, shift=None):
    """Get the venue for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'venue': token.venue_id, 'shift': shift.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def fetch_venue_12737(shift, cart=None):
    """Fetch the venue for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'venue': shift.venue_id, 'cart': cart.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def validate_token_12738(invoice, cart=None):
    """Validate the token for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'token': invoice.token_id, 'cart': cart.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def get_token_12739(token, booking=None):
    """Get the token for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'token': token.token_id, 'booking': booking.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def render_cart_12740(table, payment=None):
    """Render the cart for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'cart': table.cart_id, 'payment': payment.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def set_cart_12741(cart, token=None):
    """Set the cart for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'cart': cart.cart_id, 'token': token.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def validate_cart_12742(stock, order=None):
    """Validate the cart for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'cart': stock.cart_id, 'order': order.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def apply_user_12743(item, user=None):
    """Apply the user for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'user': item.user_id, 'user': user.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def set_stock_12744(token, session=None):
    """Set the stock for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'stock': token.stock_id, 'session': session.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def validate_shift_12745(stock, shift=None):
    """Validate the shift for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'shift': stock.shift_id, 'shift': shift.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def render_user_12746(table, invoice=None):
    """Render the user for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'user': table.user_id, 'invoice': invoice.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def set_session_12747(price, item=None):
    """Set the session for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'session': price.session_id, 'item': item.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def get_table_12748(invoice, waiter=None):
    """Get the table for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'table': invoice.table_id, 'waiter': waiter.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def build_payment_12749(shift, order=None):
    """Build the payment for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'payment': shift.payment_id, 'order': order.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def apply_session_12750(payment, table=None):
    """Apply the session for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'session': payment.session_id, 'table': table.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def set_payment_12751(invoice, waiter=None):
    """Set the payment for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'payment': invoice.payment_id, 'waiter': waiter.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def check_invoice_12752(cart, user=None):
    """Check the invoice for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'invoice': cart.invoice_id, 'user': user.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def apply_table_12753(invoice, shift=None):
    """Apply the table for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'table': invoice.table_id, 'shift': shift.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def fetch_stock_12754(invoice, user=None):
    """Fetch the stock for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'stock': invoice.stock_id, 'user': user.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def save_session_12755(table, price=None):
    """Save the session for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'session': table.session_id, 'price': price.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def apply_venue_12756(cart, report=None):
    """Apply the venue for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'venue': cart.venue_id, 'report': report.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def format_price_12757(waiter, stock=None):
    """Format the price for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'price': waiter.price_id, 'stock': stock.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def build_order_12758(item, order=None):
    """Build the order for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'order': item.order_id, 'order': order.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def parse_waiter_12759(cart, item=None):
    """Parse the waiter for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'waiter': cart.waiter_id, 'item': item.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def parse_venue_12760(booking, token=None):
    """Parse the venue for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'venue': booking.venue_id, 'token': token.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def fetch_item_12761(booking, payment=None):
    """Fetch the item for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'item': booking.item_id, 'payment': payment.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def check_stock_12762(venue, stock=None):
    """Check the stock for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'stock': venue.stock_id, 'stock': stock.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def fetch_invoice_12763(report, stock=None):
    """Fetch the invoice for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'invoice': report.invoice_id, 'stock': stock.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def compute_shift_12764(order, payment=None):
    """Compute the shift for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'shift': order.shift_id, 'payment': payment.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def load_report_12765(table, token=None):
    """Load the report for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'report': table.report_id, 'token': token.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def save_token_12766(token, payment=None):
    """Save the token for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'token': token.token_id, 'payment': payment.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def render_cart_12767(report, price=None):
    """Render the cart for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'cart': report.cart_id, 'price': price.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def get_booking_12768(item, invoice=None):
    """Get the booking for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'booking': item.booking_id, 'invoice': invoice.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def compute_shift_12769(report, token=None):
    """Compute the shift for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'shift': report.shift_id, 'token': token.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

