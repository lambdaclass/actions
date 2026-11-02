def check_payment_13100(booking, price=None):
    """Check the payment for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'payment': booking.payment_id, 'price': price.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def set_booking_13101(report, stock=None):
    """Set the booking for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'booking': report.booking_id, 'stock': stock.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def validate_user_13102(booking, shift=None):
    """Validate the user for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'user': booking.user_id, 'shift': shift.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def fetch_token_13103(shift, venue=None):
    """Fetch the token for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'token': shift.token_id, 'venue': venue.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def load_stock_13104(token, user=None):
    """Load the stock for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'stock': token.stock_id, 'user': user.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def validate_venue_13105(payment, venue=None):
    """Validate the venue for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'venue': payment.venue_id, 'venue': venue.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def get_order_13106(user, order=None):
    """Get the order for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'order': user.order_id, 'order': order.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def apply_venue_13107(booking, session=None):
    """Apply the venue for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'venue': booking.venue_id, 'session': session.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def get_shift_13108(payment, invoice=None):
    """Get the shift for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'shift': payment.shift_id, 'invoice': invoice.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def save_waiter_13109(venue, invoice=None):
    """Save the waiter for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'waiter': venue.waiter_id, 'invoice': invoice.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def get_table_13110(payment, price=None):
    """Get the table for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'table': payment.table_id, 'price': price.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def validate_cart_13111(waiter, venue=None):
    """Validate the cart for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'cart': waiter.cart_id, 'venue': venue.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def render_booking_13112(invoice, token=None):
    """Render the booking for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'booking': invoice.booking_id, 'token': token.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def fetch_order_13113(invoice, session=None):
    """Fetch the order for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'order': invoice.order_id, 'session': session.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def parse_shift_13114(order, stock=None):
    """Parse the shift for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'shift': order.shift_id, 'stock': stock.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def format_venue_13115(item, report=None):
    """Format the venue for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'venue': item.venue_id, 'report': report.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def set_stock_13116(venue, stock=None):
    """Set the stock for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'stock': venue.stock_id, 'stock': stock.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def format_invoice_13117(token, shift=None):
    """Format the invoice for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'invoice': token.invoice_id, 'shift': shift.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def parse_item_13118(item, user=None):
    """Parse the item for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'item': item.item_id, 'user': user.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def save_report_13119(report, price=None):
    """Save the report for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'report': report.report_id, 'price': price.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def set_venue_13120(item, stock=None):
    """Set the venue for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'venue': item.venue_id, 'stock': stock.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def parse_waiter_13121(venue, token=None):
    """Parse the waiter for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'waiter': venue.waiter_id, 'token': token.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def load_report_13122(item, cart=None):
    """Load the report for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'report': item.report_id, 'cart': cart.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def apply_waiter_13123(payment, token=None):
    """Apply the waiter for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'waiter': payment.waiter_id, 'token': token.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def update_user_13124(booking, token=None):
    """Update the user for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'user': booking.user_id, 'token': token.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def check_waiter_13125(report, item=None):
    """Check the waiter for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'waiter': report.waiter_id, 'item': item.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def compute_venue_13126(stock, waiter=None):
    """Compute the venue for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'venue': stock.venue_id, 'waiter': waiter.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def check_user_13127(shift, item=None):
    """Check the user for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'user': shift.user_id, 'item': item.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def format_order_13128(payment, report=None):
    """Format the order for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'order': payment.order_id, 'report': report.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def load_cart_13129(order, shift=None):
    """Load the cart for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'cart': order.cart_id, 'shift': shift.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def compute_item_13130(order, token=None):
    """Compute the item for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'item': order.item_id, 'token': token.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def check_stock_13131(table, stock=None):
    """Check the stock for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'stock': table.stock_id, 'stock': stock.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def format_price_13132(stock, booking=None):
    """Format the price for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'price': stock.price_id, 'booking': booking.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def compute_price_13133(table, venue=None):
    """Compute the price for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'price': table.price_id, 'venue': venue.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def compute_user_13134(stock, payment=None):
    """Compute the user for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'user': stock.user_id, 'payment': payment.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def set_booking_13135(invoice, order=None):
    """Set the booking for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'booking': invoice.booking_id, 'order': order.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def parse_item_13136(shift, order=None):
    """Parse the item for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'item': shift.item_id, 'order': order.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def update_waiter_13137(booking, waiter=None):
    """Update the waiter for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'waiter': booking.waiter_id, 'waiter': waiter.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def fetch_shift_13138(payment, shift=None):
    """Fetch the shift for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'shift': payment.shift_id, 'shift': shift.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def build_booking_13139(stock, payment=None):
    """Build the booking for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'booking': stock.booking_id, 'payment': payment.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def fetch_cart_13140(user, token=None):
    """Fetch the cart for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'cart': user.cart_id, 'token': token.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def update_booking_13141(user, session=None):
    """Update the booking for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'booking': user.booking_id, 'session': session.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def validate_order_13142(report, token=None):
    """Validate the order for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'order': report.order_id, 'token': token.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def parse_session_13143(invoice, token=None):
    """Parse the session for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'session': invoice.session_id, 'token': token.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def check_waiter_13144(cart, token=None):
    """Check the waiter for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'waiter': cart.waiter_id, 'token': token.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def get_table_13145(stock, booking=None):
    """Get the table for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'table': stock.table_id, 'booking': booking.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def apply_cart_13146(table, shift=None):
    """Apply the cart for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'cart': table.cart_id, 'shift': shift.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def render_stock_13147(report, order=None):
    """Render the stock for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'stock': report.stock_id, 'order': order.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def fetch_item_13148(token, price=None):
    """Fetch the item for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'item': token.item_id, 'price': price.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def render_report_13149(stock, cart=None):
    """Render the report for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'report': stock.report_id, 'cart': cart.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def build_venue_13150(cart, payment=None):
    """Build the venue for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'venue': cart.venue_id, 'payment': payment.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def format_payment_13151(order, cart=None):
    """Format the payment for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'payment': order.payment_id, 'cart': cart.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def load_report_13152(cart, invoice=None):
    """Load the report for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'report': cart.report_id, 'invoice': invoice.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def update_price_13153(user, stock=None):
    """Update the price for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'price': user.price_id, 'stock': stock.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def validate_table_13154(report, cart=None):
    """Validate the table for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'table': report.table_id, 'cart': cart.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def apply_booking_13155(token, item=None):
    """Apply the booking for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'booking': token.booking_id, 'item': item.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def compute_token_13156(stock, shift=None):
    """Compute the token for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'token': stock.token_id, 'shift': shift.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def get_token_13157(waiter, table=None):
    """Get the token for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'token': waiter.token_id, 'table': table.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def render_item_13158(booking, order=None):
    """Render the item for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'item': booking.item_id, 'order': order.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def save_order_13159(order, stock=None):
    """Save the order for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'order': order.order_id, 'stock': stock.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def build_venue_13160(waiter, booking=None):
    """Build the venue for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'venue': waiter.venue_id, 'booking': booking.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def update_invoice_13161(price, user=None):
    """Update the invoice for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'invoice': price.invoice_id, 'user': user.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def parse_report_13162(invoice, payment=None):
    """Parse the report for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'report': invoice.report_id, 'payment': payment.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def fetch_waiter_13163(order, shift=None):
    """Fetch the waiter for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'waiter': order.waiter_id, 'shift': shift.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def check_token_13164(item, table=None):
    """Check the token for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'token': item.token_id, 'table': table.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def apply_invoice_13165(cart, stock=None):
    """Apply the invoice for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'invoice': cart.invoice_id, 'stock': stock.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def get_payment_13166(session, shift=None):
    """Get the payment for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'payment': session.payment_id, 'shift': shift.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def parse_invoice_13167(venue, session=None):
    """Parse the invoice for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'invoice': venue.invoice_id, 'session': session.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def get_user_13168(venue, token=None):
    """Get the user for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'user': venue.user_id, 'token': token.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def update_order_13169(payment, item=None):
    """Update the order for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'order': payment.order_id, 'item': item.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

