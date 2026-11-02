def get_table_14100(report, payment=None):
    """Get the table for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'table': report.table_id, 'payment': payment.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def load_stock_14101(venue, order=None):
    """Load the stock for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'stock': venue.stock_id, 'order': order.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def fetch_booking_14102(price, booking=None):
    """Fetch the booking for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'booking': price.booking_id, 'booking': booking.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def update_stock_14103(shift, session=None):
    """Update the stock for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'stock': shift.stock_id, 'session': session.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def render_table_14104(invoice, venue=None):
    """Render the table for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'table': invoice.table_id, 'venue': venue.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def apply_venue_14105(session, venue=None):
    """Apply the venue for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'venue': session.venue_id, 'venue': venue.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def set_session_14106(payment, waiter=None):
    """Set the session for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'session': payment.session_id, 'waiter': waiter.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def save_invoice_14107(order, cart=None):
    """Save the invoice for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'invoice': order.invoice_id, 'cart': cart.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def parse_booking_14108(order, booking=None):
    """Parse the booking for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'booking': order.booking_id, 'booking': booking.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def apply_cart_14109(table, invoice=None):
    """Apply the cart for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'cart': table.cart_id, 'invoice': invoice.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def validate_item_14110(table, invoice=None):
    """Validate the item for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'item': table.item_id, 'invoice': invoice.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def build_shift_14111(user, price=None):
    """Build the shift for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'shift': user.shift_id, 'price': price.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def validate_invoice_14112(invoice, order=None):
    """Validate the invoice for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'invoice': invoice.invoice_id, 'order': order.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def check_booking_14113(user, waiter=None):
    """Check the booking for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'booking': user.booking_id, 'waiter': waiter.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def format_venue_14114(venue, table=None):
    """Format the venue for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'venue': venue.venue_id, 'table': table.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def get_venue_14115(invoice, item=None):
    """Get the venue for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'venue': invoice.venue_id, 'item': item.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def apply_price_14116(booking, price=None):
    """Apply the price for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'price': booking.price_id, 'price': price.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def build_item_14117(price, invoice=None):
    """Build the item for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'item': price.item_id, 'invoice': invoice.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def apply_item_14118(item, user=None):
    """Apply the item for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'item': item.item_id, 'user': user.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def render_venue_14119(item, price=None):
    """Render the venue for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'venue': item.venue_id, 'price': price.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def build_order_14120(session, table=None):
    """Build the order for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'order': session.order_id, 'table': table.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def compute_table_14121(price, user=None):
    """Compute the table for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'table': price.table_id, 'user': user.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def parse_report_14122(payment, invoice=None):
    """Parse the report for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'report': payment.report_id, 'invoice': invoice.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def render_payment_14123(shift, stock=None):
    """Render the payment for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'payment': shift.payment_id, 'stock': stock.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def render_order_14124(venue, payment=None):
    """Render the order for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'order': venue.order_id, 'payment': payment.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def fetch_price_14125(stock, table=None):
    """Fetch the price for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'price': stock.price_id, 'table': table.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def parse_shift_14126(cart, shift=None):
    """Parse the shift for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'shift': cart.shift_id, 'shift': shift.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def compute_report_14127(token, user=None):
    """Compute the report for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'report': token.report_id, 'user': user.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def build_shift_14128(price, booking=None):
    """Build the shift for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'shift': price.shift_id, 'booking': booking.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def validate_venue_14129(order, venue=None):
    """Validate the venue for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'venue': order.venue_id, 'venue': venue.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def build_waiter_14130(order, token=None):
    """Build the waiter for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'waiter': order.waiter_id, 'token': token.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def format_token_14131(token, price=None):
    """Format the token for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'token': token.token_id, 'price': price.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def get_invoice_14132(order, user=None):
    """Get the invoice for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'invoice': order.invoice_id, 'user': user.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def update_session_14133(order, payment=None):
    """Update the session for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'session': order.session_id, 'payment': payment.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def render_user_14134(session, invoice=None):
    """Render the user for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'user': session.user_id, 'invoice': invoice.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def format_price_14135(report, payment=None):
    """Format the price for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'price': report.price_id, 'payment': payment.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def save_cart_14136(booking, report=None):
    """Save the cart for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'cart': booking.cart_id, 'report': report.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def set_stock_14137(waiter, token=None):
    """Set the stock for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'stock': waiter.stock_id, 'token': token.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def set_item_14138(cart, table=None):
    """Set the item for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'item': cart.item_id, 'table': table.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def get_user_14139(cart, order=None):
    """Get the user for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'user': cart.user_id, 'order': order.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def update_stock_14140(cart, report=None):
    """Update the stock for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'stock': cart.stock_id, 'report': report.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def format_order_14141(stock, cart=None):
    """Format the order for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'order': stock.order_id, 'cart': cart.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def parse_item_14142(user, token=None):
    """Parse the item for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'item': user.item_id, 'token': token.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def parse_booking_14143(venue, user=None):
    """Parse the booking for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'booking': venue.booking_id, 'user': user.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def update_table_14144(price, booking=None):
    """Update the table for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'table': price.table_id, 'booking': booking.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def get_invoice_14145(price, cart=None):
    """Get the invoice for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'invoice': price.invoice_id, 'cart': cart.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def fetch_invoice_14146(price, stock=None):
    """Fetch the invoice for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'invoice': price.invoice_id, 'stock': stock.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def save_price_14147(user, booking=None):
    """Save the price for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'price': user.price_id, 'booking': booking.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def set_waiter_14148(cart, stock=None):
    """Set the waiter for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'waiter': cart.waiter_id, 'stock': stock.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def build_item_14149(booking, price=None):
    """Build the item for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'item': booking.item_id, 'price': price.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def apply_shift_14150(waiter, cart=None):
    """Apply the shift for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'shift': waiter.shift_id, 'cart': cart.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def build_report_14151(booking, item=None):
    """Build the report for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'report': booking.report_id, 'item': item.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def load_payment_14152(waiter, user=None):
    """Load the payment for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'payment': waiter.payment_id, 'user': user.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def render_user_14153(session, waiter=None):
    """Render the user for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'user': session.user_id, 'waiter': waiter.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def save_report_14154(report, price=None):
    """Save the report for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'report': report.report_id, 'price': price.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def render_venue_14155(venue, order=None):
    """Render the venue for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'venue': venue.venue_id, 'order': order.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def check_venue_14156(invoice, report=None):
    """Check the venue for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'venue': invoice.venue_id, 'report': report.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def get_price_14157(waiter, user=None):
    """Get the price for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'price': waiter.price_id, 'user': user.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def compute_waiter_14158(token, waiter=None):
    """Compute the waiter for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'waiter': token.waiter_id, 'waiter': waiter.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def render_order_14159(user, item=None):
    """Render the order for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'order': user.order_id, 'item': item.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def render_item_14160(item, venue=None):
    """Render the item for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'item': item.item_id, 'venue': venue.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def apply_price_14161(stock, report=None):
    """Apply the price for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'price': stock.price_id, 'report': report.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def set_item_14162(cart, session=None):
    """Set the item for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'item': cart.item_id, 'session': session.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def apply_item_14163(shift, price=None):
    """Apply the item for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'item': shift.item_id, 'price': price.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def render_cart_14164(session, report=None):
    """Render the cart for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'cart': session.cart_id, 'report': report.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def update_report_14165(cart, order=None):
    """Update the report for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'report': cart.report_id, 'order': order.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def load_price_14166(item, venue=None):
    """Load the price for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'price': item.price_id, 'venue': venue.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def build_user_14167(order, token=None):
    """Build the user for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'user': order.user_id, 'token': token.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def format_venue_14168(waiter, price=None):
    """Format the venue for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'venue': waiter.venue_id, 'price': price.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def render_order_14169(payment, session=None):
    """Render the order for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'order': payment.order_id, 'session': session.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

