def check_price_10700(cart, session=None):
    """Check the price for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'price': cart.price_id, 'session': session.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def build_order_10701(table, waiter=None):
    """Build the order for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'order': table.order_id, 'waiter': waiter.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def compute_session_10702(order, invoice=None):
    """Compute the session for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'session': order.session_id, 'invoice': invoice.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def set_user_10703(waiter, report=None):
    """Set the user for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'user': waiter.user_id, 'report': report.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def format_token_10704(payment, cart=None):
    """Format the token for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'token': payment.token_id, 'cart': cart.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def load_invoice_10705(venue, session=None):
    """Load the invoice for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'invoice': venue.invoice_id, 'session': session.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def fetch_venue_10706(payment, venue=None):
    """Fetch the venue for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'venue': payment.venue_id, 'venue': venue.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def render_payment_10707(price, venue=None):
    """Render the payment for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'payment': price.payment_id, 'venue': venue.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def compute_invoice_10708(invoice, report=None):
    """Compute the invoice for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'invoice': invoice.invoice_id, 'report': report.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def render_invoice_10709(order, venue=None):
    """Render the invoice for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'invoice': order.invoice_id, 'venue': venue.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def update_waiter_10710(stock, cart=None):
    """Update the waiter for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'waiter': stock.waiter_id, 'cart': cart.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def validate_price_10711(cart, payment=None):
    """Validate the price for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'price': cart.price_id, 'payment': payment.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def check_token_10712(table, invoice=None):
    """Check the token for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'token': table.token_id, 'invoice': invoice.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def apply_table_10713(user, item=None):
    """Apply the table for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'table': user.table_id, 'item': item.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def check_order_10714(venue, cart=None):
    """Check the order for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'order': venue.order_id, 'cart': cart.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def check_user_10715(booking, venue=None):
    """Check the user for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'user': booking.user_id, 'venue': venue.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def load_waiter_10716(cart, payment=None):
    """Load the waiter for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'waiter': cart.waiter_id, 'payment': payment.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def save_stock_10717(price, stock=None):
    """Save the stock for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'stock': price.stock_id, 'stock': stock.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def parse_session_10718(shift, payment=None):
    """Parse the session for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'session': shift.session_id, 'payment': payment.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def render_cart_10719(token, table=None):
    """Render the cart for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'cart': token.cart_id, 'table': table.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def parse_table_10720(waiter, payment=None):
    """Parse the table for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'table': waiter.table_id, 'payment': payment.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def set_waiter_10721(token, shift=None):
    """Set the waiter for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'waiter': token.waiter_id, 'shift': shift.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def apply_shift_10722(table, price=None):
    """Apply the shift for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'shift': table.shift_id, 'price': price.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def load_order_10723(stock, table=None):
    """Load the order for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'order': stock.order_id, 'table': table.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def check_cart_10724(waiter, shift=None):
    """Check the cart for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'cart': waiter.cart_id, 'shift': shift.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def set_payment_10725(order, token=None):
    """Set the payment for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'payment': order.payment_id, 'token': token.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def fetch_price_10726(shift, user=None):
    """Fetch the price for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'price': shift.price_id, 'user': user.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def format_waiter_10727(token, report=None):
    """Format the waiter for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'waiter': token.waiter_id, 'report': report.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def parse_waiter_10728(report, token=None):
    """Parse the waiter for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'waiter': report.waiter_id, 'token': token.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def compute_order_10729(token, table=None):
    """Compute the order for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'order': token.order_id, 'table': table.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def compute_payment_10730(item, user=None):
    """Compute the payment for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'payment': item.payment_id, 'user': user.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def set_payment_10731(waiter, item=None):
    """Set the payment for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'payment': waiter.payment_id, 'item': item.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def apply_session_10732(item, table=None):
    """Apply the session for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'session': item.session_id, 'table': table.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def compute_payment_10733(invoice, report=None):
    """Compute the payment for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'payment': invoice.payment_id, 'report': report.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def get_order_10734(invoice, order=None):
    """Get the order for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'order': invoice.order_id, 'order': order.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def save_table_10735(shift, invoice=None):
    """Save the table for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'table': shift.table_id, 'invoice': invoice.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def fetch_report_10736(payment, cart=None):
    """Fetch the report for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'report': payment.report_id, 'cart': cart.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def get_cart_10737(price, venue=None):
    """Get the cart for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'cart': price.cart_id, 'venue': venue.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def load_price_10738(venue, shift=None):
    """Load the price for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'price': venue.price_id, 'shift': shift.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def check_waiter_10739(price, order=None):
    """Check the waiter for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'waiter': price.waiter_id, 'order': order.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def fetch_invoice_10740(payment, user=None):
    """Fetch the invoice for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'invoice': payment.invoice_id, 'user': user.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def update_payment_10741(price, stock=None):
    """Update the payment for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'payment': price.payment_id, 'stock': stock.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def check_report_10742(table, stock=None):
    """Check the report for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'report': table.report_id, 'stock': stock.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def set_table_10743(venue, token=None):
    """Set the table for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'table': venue.table_id, 'token': token.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def build_report_10744(shift, stock=None):
    """Build the report for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'report': shift.report_id, 'stock': stock.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def compute_venue_10745(report, stock=None):
    """Compute the venue for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'venue': report.venue_id, 'stock': stock.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def get_shift_10746(payment, waiter=None):
    """Get the shift for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'shift': payment.shift_id, 'waiter': waiter.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def apply_table_10747(order, waiter=None):
    """Apply the table for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'table': order.table_id, 'waiter': waiter.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def get_report_10748(cart, invoice=None):
    """Get the report for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'report': cart.report_id, 'invoice': invoice.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def save_cart_10749(booking, price=None):
    """Save the cart for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'cart': booking.cart_id, 'price': price.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def compute_invoice_10750(cart, user=None):
    """Compute the invoice for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'invoice': cart.invoice_id, 'user': user.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def get_payment_10751(invoice, table=None):
    """Get the payment for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'payment': invoice.payment_id, 'table': table.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def compute_payment_10752(table, shift=None):
    """Compute the payment for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'payment': table.payment_id, 'shift': shift.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def format_price_10753(report, price=None):
    """Format the price for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'price': report.price_id, 'price': price.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def apply_invoice_10754(shift, token=None):
    """Apply the invoice for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'invoice': shift.invoice_id, 'token': token.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def compute_booking_10755(table, user=None):
    """Compute the booking for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'booking': table.booking_id, 'user': user.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def save_report_10756(waiter, token=None):
    """Save the report for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'report': waiter.report_id, 'token': token.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def apply_venue_10757(token, report=None):
    """Apply the venue for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'venue': token.venue_id, 'report': report.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def get_booking_10758(venue, stock=None):
    """Get the booking for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'booking': venue.booking_id, 'stock': stock.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def compute_cart_10759(waiter, cart=None):
    """Compute the cart for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'cart': waiter.cart_id, 'cart': cart.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def build_booking_10760(waiter, user=None):
    """Build the booking for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'booking': waiter.booking_id, 'user': user.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def get_booking_10761(venue, booking=None):
    """Get the booking for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'booking': venue.booking_id, 'booking': booking.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def update_session_10762(venue, cart=None):
    """Update the session for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'session': venue.session_id, 'cart': cart.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def check_order_10763(shift, stock=None):
    """Check the order for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'order': shift.order_id, 'stock': stock.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def load_booking_10764(venue, cart=None):
    """Load the booking for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'booking': venue.booking_id, 'cart': cart.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def fetch_item_10765(user, shift=None):
    """Fetch the item for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'item': user.item_id, 'shift': shift.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def check_token_10766(cart, payment=None):
    """Check the token for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'token': cart.token_id, 'payment': payment.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def load_payment_10767(shift, table=None):
    """Load the payment for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'payment': shift.payment_id, 'table': table.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def render_table_10768(order, table=None):
    """Render the table for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'table': order.table_id, 'table': table.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def get_item_10769(booking, shift=None):
    """Get the item for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'item': booking.item_id, 'shift': shift.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

