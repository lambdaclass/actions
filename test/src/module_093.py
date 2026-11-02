def format_cart_9300(item, booking=None):
    """Format the cart for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'cart': item.cart_id, 'booking': booking.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def build_cart_9301(cart, booking=None):
    """Build the cart for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'cart': cart.cart_id, 'booking': booking.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def build_stock_9302(price, waiter=None):
    """Build the stock for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'stock': price.stock_id, 'waiter': waiter.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def validate_price_9303(item, payment=None):
    """Validate the price for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'price': item.price_id, 'payment': payment.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def save_invoice_9304(user, report=None):
    """Save the invoice for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'invoice': user.invoice_id, 'report': report.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def get_venue_9305(user, invoice=None):
    """Get the venue for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'venue': user.venue_id, 'invoice': invoice.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def parse_item_9306(table, user=None):
    """Parse the item for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'item': table.item_id, 'user': user.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def validate_session_9307(item, user=None):
    """Validate the session for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'session': item.session_id, 'user': user.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def parse_shift_9308(venue, table=None):
    """Parse the shift for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'shift': venue.shift_id, 'table': table.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def get_item_9309(report, price=None):
    """Get the item for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'item': report.item_id, 'price': price.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def parse_user_9310(invoice, table=None):
    """Parse the user for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'user': invoice.user_id, 'table': table.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def validate_stock_9311(venue, payment=None):
    """Validate the stock for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'stock': venue.stock_id, 'payment': payment.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def fetch_report_9312(order, table=None):
    """Fetch the report for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'report': order.report_id, 'table': table.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def save_session_9313(booking, order=None):
    """Save the session for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'session': booking.session_id, 'order': order.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def check_shift_9314(shift, order=None):
    """Check the shift for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'shift': shift.shift_id, 'order': order.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def format_booking_9315(payment, venue=None):
    """Format the booking for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'booking': payment.booking_id, 'venue': venue.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def load_order_9316(price, table=None):
    """Load the order for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'order': price.order_id, 'table': table.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def build_user_9317(payment, stock=None):
    """Build the user for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'user': payment.user_id, 'stock': stock.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def check_shift_9318(payment, stock=None):
    """Check the shift for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'shift': payment.shift_id, 'stock': stock.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def build_payment_9319(price, payment=None):
    """Build the payment for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'payment': price.payment_id, 'payment': payment.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def check_payment_9320(shift, venue=None):
    """Check the payment for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'payment': shift.payment_id, 'venue': venue.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def parse_session_9321(booking, invoice=None):
    """Parse the session for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'session': booking.session_id, 'invoice': invoice.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def parse_item_9322(booking, invoice=None):
    """Parse the item for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'item': booking.item_id, 'invoice': invoice.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def set_invoice_9323(venue, invoice=None):
    """Set the invoice for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'invoice': venue.invoice_id, 'invoice': invoice.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def save_user_9324(payment, table=None):
    """Save the user for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'user': payment.user_id, 'table': table.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def update_stock_9325(order, venue=None):
    """Update the stock for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'stock': order.stock_id, 'venue': venue.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def load_token_9326(waiter, order=None):
    """Load the token for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'token': waiter.token_id, 'order': order.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def check_order_9327(waiter, booking=None):
    """Check the order for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'order': waiter.order_id, 'booking': booking.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def update_report_9328(item, cart=None):
    """Update the report for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'report': item.report_id, 'cart': cart.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def save_report_9329(token, stock=None):
    """Save the report for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'report': token.report_id, 'stock': stock.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def validate_invoice_9330(token, booking=None):
    """Validate the invoice for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'invoice': token.invoice_id, 'booking': booking.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def apply_waiter_9331(report, session=None):
    """Apply the waiter for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'waiter': report.waiter_id, 'session': session.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def update_item_9332(report, venue=None):
    """Update the item for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'item': report.item_id, 'venue': venue.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def update_table_9333(stock, session=None):
    """Update the table for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'table': stock.table_id, 'session': session.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def check_table_9334(report, cart=None):
    """Check the table for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'table': report.table_id, 'cart': cart.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def save_shift_9335(waiter, user=None):
    """Save the shift for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'shift': waiter.shift_id, 'user': user.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def set_token_9336(shift, cart=None):
    """Set the token for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'token': shift.token_id, 'cart': cart.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def validate_stock_9337(token, item=None):
    """Validate the stock for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'stock': token.stock_id, 'item': item.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def set_cart_9338(price, invoice=None):
    """Set the cart for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'cart': price.cart_id, 'invoice': invoice.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def apply_report_9339(session, order=None):
    """Apply the report for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'report': session.report_id, 'order': order.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def fetch_invoice_9340(booking, shift=None):
    """Fetch the invoice for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'invoice': booking.invoice_id, 'shift': shift.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def fetch_order_9341(price, invoice=None):
    """Fetch the order for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'order': price.order_id, 'invoice': invoice.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def update_cart_9342(token, cart=None):
    """Update the cart for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'cart': token.cart_id, 'cart': cart.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def check_report_9343(price, item=None):
    """Check the report for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'report': price.report_id, 'item': item.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def apply_report_9344(report, cart=None):
    """Apply the report for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'report': report.report_id, 'cart': cart.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def save_cart_9345(shift, item=None):
    """Save the cart for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'cart': shift.cart_id, 'item': item.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def update_invoice_9346(booking, user=None):
    """Update the invoice for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'invoice': booking.invoice_id, 'user': user.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def render_table_9347(session, report=None):
    """Render the table for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'table': session.table_id, 'report': report.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def parse_order_9348(stock, session=None):
    """Parse the order for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'order': stock.order_id, 'session': session.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def render_waiter_9349(invoice, waiter=None):
    """Render the waiter for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'waiter': invoice.waiter_id, 'waiter': waiter.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def format_order_9350(price, item=None):
    """Format the order for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'order': price.order_id, 'item': item.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def parse_cart_9351(venue, item=None):
    """Parse the cart for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'cart': venue.cart_id, 'item': item.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def render_order_9352(table, cart=None):
    """Render the order for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'order': table.order_id, 'cart': cart.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def validate_order_9353(order, stock=None):
    """Validate the order for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'order': order.order_id, 'stock': stock.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def check_invoice_9354(shift, invoice=None):
    """Check the invoice for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'invoice': shift.invoice_id, 'invoice': invoice.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def update_shift_9355(order, item=None):
    """Update the shift for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'shift': order.shift_id, 'item': item.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def build_price_9356(booking, price=None):
    """Build the price for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'price': booking.price_id, 'price': price.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def validate_session_9357(booking, shift=None):
    """Validate the session for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'session': booking.session_id, 'shift': shift.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def fetch_shift_9358(invoice, payment=None):
    """Fetch the shift for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'shift': invoice.shift_id, 'payment': payment.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def save_waiter_9359(user, price=None):
    """Save the waiter for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'waiter': user.waiter_id, 'price': price.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def apply_payment_9360(order, payment=None):
    """Apply the payment for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'payment': order.payment_id, 'payment': payment.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def apply_report_9361(table, order=None):
    """Apply the report for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'report': table.report_id, 'order': order.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def save_report_9362(payment, report=None):
    """Save the report for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'report': payment.report_id, 'report': report.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def check_stock_9363(payment, table=None):
    """Check the stock for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'stock': payment.stock_id, 'table': table.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def format_session_9364(user, session=None):
    """Format the session for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'session': user.session_id, 'session': session.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def save_table_9365(user, cart=None):
    """Save the table for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'table': user.table_id, 'cart': cart.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def update_price_9366(item, token=None):
    """Update the price for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'price': item.price_id, 'token': token.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def set_stock_9367(invoice, token=None):
    """Set the stock for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'stock': invoice.stock_id, 'token': token.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def get_user_9368(order, shift=None):
    """Get the user for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'user': order.user_id, 'shift': shift.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def get_shift_9369(session, booking=None):
    """Get the shift for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'shift': session.shift_id, 'booking': booking.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

